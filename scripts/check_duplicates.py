#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检测章节内与章节间的重复句子/段落（用于条件1：无章内/跨章重复）"""
import re, sys
from pathlib import Path

def cjk(s): return re.findall(r'[\u4e00-\u9fff]', s)

def sents(text):
    # 以。！？和换行切分句子，保留标点
    parts = re.split(r'(?<=[。！？])', text)
    out = []
    for p in parts:
        p = p.strip()
        if len(cjk(p)) >= 12:   # 只检测>=12汉字的句子
            out.append(p)
    return out

def main():
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    files = sorted(d.glob('第*.md'))
    all_sents = {}   # file -> [sent]
    for f in files:
        txt = f.read_text(encoding='utf-8')
        # 去掉标题/概要/备注等元数据，仅检测正文
        body = re.sub(r'#.*', '', txt)
        body = re.sub(r'- \*\*.*?\*\*', '', body)
        s = sents(body)
        all_sents[f.name] = s

    # 1) 章内重复
    print('===== 章内重复 (>=12汉字, 出现>=2次) =====')
    intra_total = 0
    for fn, s in all_sents.items():
        seen = {}
        for x in s:
            seen[x] = seen.get(x, 0) + 1
        dups = {k:v for k,v in seen.items() if v >= 2}
        if dups:
            intra_total += len(dups)
            print(f'\n[{fn}]')
            for k,v in dups.items():
                print(f'  ({v}次) {k[:50]}')

    # 2) 跨章重复 (相同句子出现在不同文件)
    print('\n===== 跨章重复 (相同句出现在>=2个文件) =====')
    inter = {}
    for fn, s in all_sents.items():
        for x in set(s):
            inter.setdefault(x, set()).add(fn)
    inter_total = 0
    for x, fns in inter.items():
        if len(fns) >= 2:
            inter_total += 1
            print(f'\n  ({len(fns)}章) {x[:60]}')
            for f in sorted(fns):
                print(f'      - {f}')
    print(f'\n总计: 章内重复 {intra_total} 处, 跨章重复 {inter_total} 处')

if __name__ == '__main__':
    main()
