import torch
import torch.nn as nn
from torch.nn import functional as F


# --------------------------------------------------
# Configuration
# --------------------------------------------------

CHECKPOINT_PATH = "mini_gpt2_shakespeare.pt"

device = "cuda" if torch.cuda.is_available() else "cpu"


# --------------------------------------------------
# Load checkpoint
# --------------------------------------------------

checkpoint = torch.load(
    CHECKPOINT_PATH,
    map_location=device,
    weights_only=False
)

vocab_size = checkpoint["vocab_size"]
n_embd = checkpoint["n_embd"]
n_head = checkpoint["n_head"]
n_layer = checkpoint["n_layer"]
block_size = checkpoint["block_size"]
dropout = checkpoint["dropout"]

stoi = checkpoint["stoi"]
itos = checkpoint["itos"]


# --------------------------------------------------
# Encoder / Decoder
# --------------------------------------------------

def encode(text):
    return [stoi[c] for c in text]


def decode(tokens):
    return "".join(itos[i] for i in tokens)


# --------------------------------------------------
# Causal Self-Attention Head
# --------------------------------------------------

class Head(nn.Module):

    def __init__(self, head_size):
        super().__init__()

        self.key = nn.Linear(
            n_embd,
            head_size,
            bias=False
        )

        self.query = nn.Linear(
            n_embd,
            head_size,
            bias=False
        )

        self.value = nn.Linear(
            n_embd,
            head_size,
            bias=False
        )

        self.register_buffer(
            "tril",
            torch.tril(
                torch.ones(
                    block_size,
                    block_size
                )
            )
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        B, T, C = x.shape

        k = self.key(x)
        q = self.query(x)

        wei = q @ k.transpose(-2, -1)

        wei = wei * (C ** -0.5)

        wei = wei.masked_fill(
            self.tril[:T, :T] == 0,
            float("-inf")
        )

        wei = F.softmax(
            wei,
            dim=-1
        )

        wei = self.dropout(wei)

        v = self.value(x)

        return wei @ v


# --------------------------------------------------
# Multi-Head Attention
# --------------------------------------------------

class MultiHeadAttention(nn.Module):

    def __init__(
        self,
        num_heads,
        head_size
    ):
        super().__init__()

        self.heads = nn.ModuleList(
            [
                Head(head_size)
                for _ in range(num_heads)
            ]
        )

        self.proj = nn.Linear(
            num_heads * head_size,
            n_embd
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        out = torch.cat(
            [head(x) for head in self.heads],
            dim=-1
        )

        out = self.proj(out)

        return self.dropout(out)


# --------------------------------------------------
# Feed Forward Network
# --------------------------------------------------

class FeedForward(nn.Module):

    def __init__(self, n_embd):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(
                n_embd,
                4 * n_embd
            ),

            nn.ReLU(),

            nn.Linear(
                4 * n_embd,
                n_embd
            ),

            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.net(x)


# --------------------------------------------------
# Transformer Block
# --------------------------------------------------

class Block(nn.Module):

    def __init__(
        self,
        n_embd,
        n_head
    ):
        super().__init__()

        head_size = n_embd // n_head

        self.sa = MultiHeadAttention(
            n_head,
            head_size
        )

        self.ffwd = FeedForward(
            n_embd
        )

        self.ln1 = nn.LayerNorm(
            n_embd
        )

        self.ln2 = nn.LayerNorm(
            n_embd
        )

    def forward(self, x):

        x = x + self.sa(
            self.ln1(x)
        )

        x = x + self.ffwd(
            self.ln2(x)
        )

        return x


# --------------------------------------------------
# GPT Language Model
# --------------------------------------------------

class GPTLanguageModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.token_embedding_table = nn.Embedding(
            vocab_size,
            n_embd
        )

        self.position_embedding_table = nn.Embedding(
            block_size,
            n_embd
        )

        self.blocks = nn.Sequential(
            *[
                Block(
                    n_embd,
                    n_head
                )
                for _ in range(n_layer)
            ]
        )

        self.ln_f = nn.LayerNorm(
            n_embd
        )

        self.lm_head = nn.Linear(
            n_embd,
            vocab_size
        )

    def forward(
        self,
        idx
    ):

        B, T = idx.shape

        tok_emb = self.token_embedding_table(
            idx
        )

        pos_emb = self.position_embedding_table(
            torch.arange(
                T,
                device=device
            )
        )

        x = tok_emb + pos_emb

        x = self.blocks(x)

        x = self.ln_f(x)

        logits = self.lm_head(x)

        return logits

    @torch.no_grad()
    def generate(
        self,
        idx,
        max_new_tokens,
        temperature=0.8
    ):

        for _ in range(max_new_tokens):

            idx_cond = idx[:, -block_size:]

            logits = self(
                idx_cond
            )

            logits = logits[:, -1, :]

            logits = logits / temperature

            probs = F.softmax(
                logits,
                dim=-1
            )

            idx_next = torch.multinomial(
                probs,
                num_samples=1
            )

            idx = torch.cat(
                [idx, idx_next],
                dim=1
            )

        return idx


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

model = GPTLanguageModel()

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.to(device)

model.eval()


# --------------------------------------------------
# Public generation function
# --------------------------------------------------

def generate_text(
    prompt,
    max_new_tokens=300,
    temperature=0.8
):

    if not prompt:
        prompt = "ROMEO:"

    # Keep only characters known to tokenizer
    prompt = "".join(
        c for c in prompt
        if c in stoi
    )

    if not prompt:
        prompt = "ROMEO:"

    context = torch.tensor(
        [encode(prompt)],
        dtype=torch.long,
        device=device
    )

    generated = model.generate(
        context,
        max_new_tokens=max_new_tokens,
        temperature=temperature
    )

    return decode(
        generated[0].tolist()
    )