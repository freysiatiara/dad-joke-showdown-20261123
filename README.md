# Dad Joke Showdown

![make.fun bounty](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)
![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/freysiatiara/dad-joke-showdown-20261123/rank.svg)
![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/freysiatiara/dad-joke-showdown-20261123/reward.svg)

Entry for the make.fun bounty [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5).

One original dad joke, 86 characters, told in a father's straight-faced
voice across the dinner table:

> My GPS and I broke up — it kept telling me where to go, so I took its advice and left.

The pun turns on "telling me where to go": navigation directions on the
surface, a rude dismissal underneath. No recycled classic, no setup
longer than it needs to be — the punchline arrives at the very end.

`main.py` (stdlib only) writes the joke to the output path
(`/output/entry.txt` by default; `ENTRY_OUTPUT` / `OUTPUT_DIR` /
`MAKEFUN_OUTPUT_DIR` override it). It self-checks the gate before
writing: 1–200 characters, not only whitespace, a single line, and
verifies the written output round-trips byte-identical.
