// news-image-20261120 entry program.
//
// Friday 20 November 2026, summed up in one picture: entry.png in this
// repository is a hand-drawn newspaper front page with five stories from
// that day (a cyclone landfall in India, missiles over Kyiv, Trump on
// Iran, a Houthi strike on Riyadh, and COP31 closing in Antalya).
//
// This program does nothing clever: it drops a copy of that image at
// $MAKEFUN_OUTPUT_DIR/entry.png, where the grader looks for it. It uses
// only the Node standard library, touches no network, and always writes
// the same bytes, so running it twice gives identical output.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
// copyFileSync moves the bytes unchanged, so the output is identical
// to the image in this repository on every run.
copyFileSync(join(here, "entry.png"), target);
