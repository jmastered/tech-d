{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import string, itertools\
\
def o(f, k): return ''.join(k[i % len(k)] for i in range(len(f)))\
def c(t, k, b): return ''.join(chr((ord(j) + b * (ord(k[i % len(k)]) - ord('A'))) % 26 + ord('A')) if j.isalpha() else j for i, j in enumerate(t.upper()))\
if __name__ == "__main__": p, k = "Hello, World!", "KEY"; e = c(p, o(p, k), 1); print("E:", e); print("D:", c(e, o(e, k), -1))\
}