from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts('i8pOulVUz0A')
transcript = transcript_list.find_transcript(['en'])
transcript = transcript.fetch()

with open("transcript.txt", 'w') as f:
    for line in transcript:
        f.write(line['text']+ '\n')