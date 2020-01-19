# Synviz
Synviz is a system for in-person lip-reading. It takes video footage from a camera mounted on a pair of glasses, and passes that
data to a backend that reads the lips of a subject in the video footage.

## Final Product
This is a fairly early prototype, but we believe the idea is worth pursuing. With better hardware,
the whole pipeline would take less than a second, allowing for real-time subtitling. With a stronger on-board battery,
5G wifi speeds, and a computationally strong server, this prototype would turn into a viable product.
### North Focals
There's a company in Waterloo that's producing smart glasses that would be an amazing paring with this technology.
North Focals have a heads-up display worked in. This would be ideal for this pipeline: We could attach a camera,
record the video, process it, and then send it back to the glasses to provide real-time subtitling.

## Social Impact
This hack can actually help in situations where communication is difficult. By far the best use case is when
this technology is combined with automatic speech recognition. All-in-one solutions for real-time transcription and translation
are becoming more and more viable as our technology progresses. We've come a long way from Google Glass. 
This proof-of-concept is another key piece that would
improve human computer interaction.

## Quick Pipeline Overview
* The user presses a button to start a recording.
* The user clicks the button again to stop recording
* The data is passed to a Google Cloud Platform bucket as a numpy array file
* Simultaneously, the glasses ping the Flask backend server to let it know there's something to be processed
* The backend downloads the video numpy array.
* The backend runs the video through a Haar Cascade Network to detect a face.
* The video is cropped so that it tracks the mouth of the speaker
* The cropped video is fed through a transformer network to get a transcript
* The backend passes the transcript to the frontend through a socket
* Simultaneously, the backend uploads an mp4 video to Google Cloud Platform
* The frontend displays the transcript it got from the backend, and also displays the 
mp4 file found on Google Cloud Platform

## Use Cases
This system has a few use cases:
* individuals who are hard-of hearing or deaf
* noisy environments where automatic speech recognition is impossible
* combined with speech recognition for ultra-accurate, real-time transcripts.
* Language learners who want a transcript or translation

## Inspiration
We were inspired to do this hack from a really interesting paper published by NVidia researchers.
We present a use-case for their lip-reading Transformer network. Here's the paper:
