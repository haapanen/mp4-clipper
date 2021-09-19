#!/usr/bin/env python3

import click
import os

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


@click.command()
@click.option("--clip", required=True)
@click.option("--output", default="clip.mp4")
@click.option("--overwrite", default=False)
@click.option("--start", default=None, help="Start time in seconds since the beginning of the video")
@click.option("--end", default=None, help="End time in seconds since the beginning of the video")
def cli(clip: str, output: str, overwrite: bool, start: int, end: int):
    if not os.path.exists(clip) or not os.path.isfile(clip):
        print(f"{clip} does not exist")
        exit(1)
    
    if len(output) == 0:
        print("output must be specified")
        exit(2)
    
    copy_number = 1
    if not overwrite and os.path.exists(output):
        print(f"{output} already exists")
        exit(3)

    if not output.lower().endswith(".mp4"):
        output = output + ".mp4"
    
    ffmpeg_extract_subclip(clip, int(start), int(end), targetname=output)
    print(f"Saved to {output}")

if __name__ == "__main__":
    cli()