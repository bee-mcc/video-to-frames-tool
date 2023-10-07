# video-to-frames-tool

This is a tool to create videos by selecting and lengthening the duration of random frames from a source video

## Use cases and examples

This program can create some pretty trippy videos from old media. See [example 1](https://www.reddit.com/user/bee_mcc_webdev/comments/16fawo9/frame_reducer_example_1/?utm_source=share&utm_medium=web2x&context=3). Furthermore, this tool could be enhanced to "comic-i-fy" any type of video.

## Instructions

1. Install dependencies

2. Configure the program to take in your source video and run main.py

3. Rip audio from your source video using ffmpeg

4. Collate frame output into video using ffmpeg (after getting details from source video)

## Useful commands

Information about file
`ffprobe`

Rip audio from file (check audio codec and associated file extension first)
` ffmpeg -i example.mkv -vn -acodec copy output-audio.eac3`

Collate frames into video (check video codec, framerate, and pixel format to use)
`ffmpeg -framerate 30 -i 'frame%d.jpg' \ -i output-audio.eac3 -c:a copy -shortest -c:v h264 -pix_fmt yuv420p out.mp4`

Can also use glob matching if output frame images in different format

`ffmpeg -framerate 30 -pattern_type glob -i 'frame*.jpg' \ -i output-audio.eac3 -c:a copy -shortest -c:v h264 -pix_fmt yuv420p out.mp4`

## Background

I was over at a friend's house one evening, and we were trying to watch an episode of Spongebob. His computer had some issue preventing the video from loading more than a frame or two every two or three seconds, but it loaded the audio fine. I thought it was the most hilarious thing at the time... so I decided to recreate it. Simple code is cool.
