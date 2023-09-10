# video-to-frames-tool

This is a tool to create videos by selecting and lengthening the duration of random frames from a source video

## Use cases and examples

This program can create some pretty trippy videos from old media. See example 1, example 2, example 3. Furthermore, this tool could be enhanced to "comic-i-fy" any type of video.

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
