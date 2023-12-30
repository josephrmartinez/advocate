def process_transcript(transcript):
    
    transcript_strings = []
    
    for entry in transcript:
        speaker = entry["speaker"]
        text = entry["text"]

        # Convert the "end" value to seconds as a floating-point number
        seconds_float = float(entry["end"])

        # Round or truncate the floating-point number to get an integer value
        seconds = round(seconds_float)  # or int(seconds_float)

        # Convert seconds to hours, minutes, and seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        timestamp = "[{:02d}:{:02d}:{:02d}]".format(hours, minutes, seconds)

        transcript_strings.append(f"**{speaker}**: {text} {timestamp}")
        
    clean_transcript = "\n\n".join(transcript_strings)
    
    # with open(f"./podcasts-clean-transcripts/{episode_name}.md", "w") as f:    
    #     f.write(clean_transcript)
        
    return clean_transcript


mp3transcript = [
        {
          "end": "27.64",
          "text": "I am Dr. Salisbury's resident. So, I just have a few questions for you with the fertility stuff. When did you start having that issues? Are you having any issues at all, any symptoms at all?",
          "start": "12.56",
          "words": [
            {
              "end": 12.9,
              "word": "I",
              "start": 12.56
            },
            {
              "end": 13.22,
              "word": "am",
              "start": 12.9
            },
            {
              "end": 13.6,
              "word": "Dr.",
              "start": 13.22
            },
            {
              "end": 14.32,
              "word": "Salisbury's",
              "start": 13.84
            },
            {
              "end": 14.62,
              "word": "resident.",
              "start": 14.32
            },
            {
              "end": 16.8,
              "word": "So,",
              "start": 16.32
            },
            {
              "end": 16.92,
              "word": "I",
              "start": 16.8
            },
            {
              "end": 16.96,
              "word": "just",
              "start": 16.92
            },
            {
              "end": 17.08,
              "word": "have",
              "start": 16.96
            },
            {
              "end": 17.18,
              "word": "a",
              "start": 17.08
            },
            {
              "end": 17.42,
              "word": "few",
              "start": 17.18
            },
            {
              "end": 17.86,
              "word": "questions",
              "start": 17.42
            },
            {
              "end": 18.14,
              "word": "for",
              "start": 17.86
            },
            {
              "end": 18.52,
              "word": "you",
              "start": 18.14
            },
            {
              "end": 19.2,
              "word": "with",
              "start": 18.52
            },
            {
              "end": 19.28,
              "word": "the",
              "start": 19.2
            },
            {
              "end": 19.7,
              "word": "fertility",
              "start": 19.28
            },
            {
              "end": 20.2,
              "word": "stuff.",
              "start": 19.7
            },
            {
              "end": 22.42,
              "word": "When",
              "start": 21.94
            },
            {
              "end": 22.9,
              "word": "did",
              "start": 22.42
            },
            {
              "end": 23.16,
              "word": "you",
              "start": 22.9
            },
            {
              "end": 23.48,
              "word": "start",
              "start": 23.16
            },
            {
              "end": 24,
              "word": "having",
              "start": 23.48
            },
            {
              "end": 24.42,
              "word": "that",
              "start": 24
            },
            {
              "end": 24.92,
              "word": "issues?",
              "start": 24.42
            },
            {
              "end": 25.32,
              "word": "Are",
              "start": 25.12
            },
            {
              "end": 25.42,
              "word": "you",
              "start": 25.32
            },
            {
              "end": 25.6,
              "word": "having",
              "start": 25.42
            },
            {
              "end": 25.84,
              "word": "any",
              "start": 25.6
            },
            {
              "end": 26.24,
              "word": "issues",
              "start": 25.84
            },
            {
              "end": 26.46,
              "word": "at",
              "start": 26.24
            },
            {
              "end": 26.66,
              "word": "all,",
              "start": 26.46
            },
            {
              "end": 26.8,
              "word": "any",
              "start": 26.68
            },
            {
              "end": 27.2,
              "word": "symptoms",
              "start": 26.8
            },
            {
              "end": 27.46,
              "word": "at",
              "start": 27.2
            },
            {
              "end": 27.64,
              "word": "all?",
              "start": 27.46
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "84.74",
          "text": "No. So, sorry. The issue, we don't yet understand what the real issue is. So, I have never got, I have not gotten any results back from semen analysis. So, I don't know from the male partner's side of things. I don't know if I am contributing anything. Okay. We've taken those tests, should get those results within the next day or so. Okay. So, that's the male side of things. On the female side of things, my partner had a ruptured appendix and she was like, oh, no. Kid. Okay. We've spoken in person to a fertility doctor who discussed that he anecdotally has an understanding that women with severely ruptured appendices can sometimes like, can basically damage some of the, I'm sorry, I'm spacing on like the specific parts.",
          "start": "28.84",
          "words": [
            {
              "end": 29.32,
              "word": "No.",
              "start": 28.84
            },
            {
              "end": 29.62,
              "word": "So,",
              "start": 29.4
            },
            {
              "end": 30.1,
              "word": "sorry.",
              "start": 29.7
            },
            {
              "end": 30.34,
              "word": "The",
              "start": 30.1
            },
            {
              "end": 30.88,
              "word": "issue,",
              "start": 30.34
            },
            {
              "end": 32.9,
              "word": "we",
              "start": 31.22
            },
            {
              "end": 33.18,
              "word": "don't",
              "start": 32.9
            },
            {
              "end": 33.44,
              "word": "yet",
              "start": 33.18
            },
            {
              "end": 34.08,
              "word": "understand",
              "start": 33.44
            },
            {
              "end": 34.8,
              "word": "what",
              "start": 34.08
            },
            {
              "end": 35,
              "word": "the",
              "start": 34.8
            },
            {
              "end": 35.28,
              "word": "real",
              "start": 35
            },
            {
              "end": 35.66,
              "word": "issue",
              "start": 35.28
            },
            {
              "end": 35.98,
              "word": "is.",
              "start": 35.66
            },
            {
              "end": 36.36,
              "word": "So,",
              "start": 36.14
            },
            {
              "end": 36.84,
              "word": "I",
              "start": 36.4
            },
            {
              "end": 37.12,
              "word": "have",
              "start": 36.84
            },
            {
              "end": 37.36,
              "word": "never",
              "start": 37.12
            },
            {
              "end": 37.64,
              "word": "got,",
              "start": 37.36
            },
            {
              "end": 37.8,
              "word": "I",
              "start": 37.7
            },
            {
              "end": 37.92,
              "word": "have",
              "start": 37.8
            },
            {
              "end": 38.12,
              "word": "not",
              "start": 37.92
            },
            {
              "end": 38.42,
              "word": "gotten",
              "start": 38.12
            },
            {
              "end": 38.64,
              "word": "any",
              "start": 38.42
            },
            {
              "end": 38.94,
              "word": "results",
              "start": 38.64
            },
            {
              "end": 39.3,
              "word": "back",
              "start": 38.94
            },
            {
              "end": 39.62,
              "word": "from",
              "start": 39.3
            },
            {
              "end": 39.94,
              "word": "semen",
              "start": 39.62
            },
            {
              "end": 40.28,
              "word": "analysis.",
              "start": 39.94
            },
            {
              "end": 40.94,
              "word": "So,",
              "start": 40.64
            },
            {
              "end": 41.08,
              "word": "I",
              "start": 41.02
            },
            {
              "end": 41.26,
              "word": "don't",
              "start": 41.08
            },
            {
              "end": 41.42,
              "word": "know",
              "start": 41.26
            },
            {
              "end": 41.58,
              "word": "from",
              "start": 41.42
            },
            {
              "end": 41.76,
              "word": "the",
              "start": 41.58
            },
            {
              "end": 41.98,
              "word": "male",
              "start": 41.76
            },
            {
              "end": 42.74,
              "word": "partner's",
              "start": 41.98
            },
            {
              "end": 43.12,
              "word": "side",
              "start": 42.74
            },
            {
              "end": 43.28,
              "word": "of",
              "start": 43.12
            },
            {
              "end": 43.5,
              "word": "things.",
              "start": 43.28
            },
            {
              "end": 44.22,
              "word": "I",
              "start": 43.74
            },
            {
              "end": 44.42,
              "word": "don't",
              "start": 44.22
            },
            {
              "end": 44.56,
              "word": "know",
              "start": 44.42
            },
            {
              "end": 44.72,
              "word": "if",
              "start": 44.56
            },
            {
              "end": 44.8,
              "word": "I",
              "start": 44.72
            },
            {
              "end": 44.96,
              "word": "am",
              "start": 44.8
            },
            {
              "end": 45.4,
              "word": "contributing",
              "start": 44.96
            },
            {
              "end": 46.24,
              "word": "anything.",
              "start": 45.4
            },
            {
              "end": 47.32,
              "word": "Okay.",
              "start": 46.84
            },
            {
              "end": 47.44,
              "word": "We've",
              "start": 47.32
            },
            {
              "end": 47.88,
              "word": "taken",
              "start": 47.44
            },
            {
              "end": 48.1,
              "word": "those",
              "start": 47.88
            },
            {
              "end": 48.62,
              "word": "tests,",
              "start": 48.1
            },
            {
              "end": 49.5,
              "word": "should",
              "start": 48.82
            },
            {
              "end": 49.68,
              "word": "get",
              "start": 49.5
            },
            {
              "end": 49.92,
              "word": "those",
              "start": 49.68
            },
            {
              "end": 50.3,
              "word": "results",
              "start": 49.92
            },
            {
              "end": 50.72,
              "word": "within",
              "start": 50.3
            },
            {
              "end": 50.9,
              "word": "the",
              "start": 50.72
            },
            {
              "end": 51.14,
              "word": "next",
              "start": 50.9
            },
            {
              "end": 51.64,
              "word": "day",
              "start": 51.14
            },
            {
              "end": 51.8,
              "word": "or",
              "start": 51.64
            },
            {
              "end": 52,
              "word": "so.",
              "start": 51.8
            },
            {
              "end": 52.74,
              "word": "Okay.",
              "start": 52.26
            },
            {
              "end": 52.96,
              "word": "So,",
              "start": 52.8
            },
            {
              "end": 53.16,
              "word": "that's",
              "start": 53
            },
            {
              "end": 53.76,
              "word": "the",
              "start": 53.16
            },
            {
              "end": 54.02,
              "word": "male",
              "start": 53.76
            },
            {
              "end": 54.3,
              "word": "side",
              "start": 54.02
            },
            {
              "end": 54.44,
              "word": "of",
              "start": 54.3
            },
            {
              "end": 54.56,
              "word": "things.",
              "start": 54.44
            },
            {
              "end": 55.18,
              "word": "On",
              "start": 54.7
            },
            {
              "end": 55.34,
              "word": "the",
              "start": 55.18
            },
            {
              "end": 55.52,
              "word": "female",
              "start": 55.34
            },
            {
              "end": 55.74,
              "word": "side",
              "start": 55.52
            },
            {
              "end": 55.92,
              "word": "of",
              "start": 55.74
            },
            {
              "end": 56.14,
              "word": "things,",
              "start": 55.92
            },
            {
              "end": 56.76,
              "word": "my",
              "start": 56.36
            },
            {
              "end": 57.12,
              "word": "partner",
              "start": 56.76
            },
            {
              "end": 57.38,
              "word": "had",
              "start": 57.12
            },
            {
              "end": 57.58,
              "word": "a",
              "start": 57.38
            },
            {
              "end": 57.96,
              "word": "ruptured",
              "start": 57.58
            },
            {
              "end": 58.76,
              "word": "appendix",
              "start": 57.96
            },
            {
              "end": 59.28,
              "word": "and",
              "start": 58.76
            },
            {
              "end": 59.48,
              "word": "she",
              "start": 59.28
            },
            {
              "end": 59.64,
              "word": "was",
              "start": 59.48
            },
            {
              "end": 59.96,
              "word": "like,",
              "start": 59.64
            },
            {
              "end": 60.08,
              "word": "oh,",
              "start": 59.96
            },
            {
              "end": 60.68,
              "word": "no.",
              "start": 60.1
            },
            {
              "end": 61.38,
              "word": "Kid.",
              "start": 60.94
            },
            {
              "end": 62.16,
              "word": "Okay.",
              "start": 61.6
            },
            {
              "end": 63.12,
              "word": "We've",
              "start": 62.4
            },
            {
              "end": 63.84,
              "word": "spoken",
              "start": 63.12
            },
            {
              "end": 64.2,
              "word": "in",
              "start": 63.84
            },
            {
              "end": 64.68,
              "word": "person",
              "start": 64.2
            },
            {
              "end": 65.02,
              "word": "to",
              "start": 64.68
            },
            {
              "end": 65.14,
              "word": "a",
              "start": 65.02
            },
            {
              "end": 65.48,
              "word": "fertility",
              "start": 65.14
            },
            {
              "end": 65.86,
              "word": "doctor",
              "start": 65.48
            },
            {
              "end": 66.22,
              "word": "who",
              "start": 65.86
            },
            {
              "end": 66.66,
              "word": "discussed",
              "start": 66.22
            },
            {
              "end": 67.56,
              "word": "that",
              "start": 66.66
            },
            {
              "end": 68,
              "word": "he",
              "start": 67.56
            },
            {
              "end": 69.74,
              "word": "anecdotally",
              "start": 68
            },
            {
              "end": 71.54,
              "word": "has",
              "start": 69.74
            },
            {
              "end": 71.78,
              "word": "an",
              "start": 71.54
            },
            {
              "end": 72.14,
              "word": "understanding",
              "start": 71.78
            },
            {
              "end": 73.02,
              "word": "that",
              "start": 72.66
            },
            {
              "end": 73.86,
              "word": "women",
              "start": 73.02
            },
            {
              "end": 74.26,
              "word": "with",
              "start": 73.86
            },
            {
              "end": 74.82,
              "word": "severely",
              "start": 74.26
            },
            {
              "end": 75.4,
              "word": "ruptured",
              "start": 74.82
            },
            {
              "end": 75.86,
              "word": "appendices",
              "start": 75.4
            },
            {
              "end": 76.3,
              "word": "can",
              "start": 75.86
            },
            {
              "end": 76.6,
              "word": "sometimes",
              "start": 76.3
            },
            {
              "end": 76.98,
              "word": "like,",
              "start": 76.6
            },
            {
              "end": 77.64,
              "word": "can",
              "start": 77
            },
            {
              "end": 78.02,
              "word": "basically",
              "start": 77.64
            },
            {
              "end": 78.54,
              "word": "damage",
              "start": 78.02
            },
            {
              "end": 79.48,
              "word": "some",
              "start": 79.12
            },
            {
              "end": 79.62,
              "word": "of",
              "start": 79.48
            },
            {
              "end": 79.76,
              "word": "the,",
              "start": 79.62
            },
            {
              "end": 82.04,
              "word": "I'm",
              "start": 79.84
            },
            {
              "end": 82.38,
              "word": "sorry,",
              "start": 82.04
            },
            {
              "end": 82.64,
              "word": "I'm",
              "start": 82.54
            },
            {
              "end": 82.86,
              "word": "spacing",
              "start": 82.64
            },
            {
              "end": 83.16,
              "word": "on",
              "start": 82.86
            },
            {
              "end": 83.34,
              "word": "like",
              "start": 83.16
            },
            {
              "end": 83.48,
              "word": "the",
              "start": 83.34
            },
            {
              "end": 83.86,
              "word": "specific",
              "start": 83.48
            },
            {
              "end": 84.74,
              "word": "parts.",
              "start": 83.86
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "87.96",
          "text": "The ovaries or the uterus or what? No.",
          "start": "84.8",
          "words": [
            {
              "end": 85.34,
              "word": "The",
              "start": 84.8
            },
            {
              "end": 85.9,
              "word": "ovaries",
              "start": 85.34
            },
            {
              "end": 86.14,
              "word": "or",
              "start": 85.9
            },
            {
              "end": 86.38,
              "word": "the",
              "start": 86.14
            },
            {
              "end": 87.22,
              "word": "uterus",
              "start": 86.38
            },
            {
              "end": 87.4,
              "word": "or",
              "start": 87.22
            },
            {
              "end": 87.62,
              "word": "what?",
              "start": 87.4
            },
            {
              "end": 87.96,
              "word": "No.",
              "start": 87.78
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "118.68",
          "text": "No. No. The condition of her uterus is good. Her tubes, they did like an HSG and like the tubes are healthy. It's really like at the end of the tubes, there's like these little fibrae that need to be, they need, they perform this one task of basically like picking up the egg. Eggs, right. And he said that anecdotally, people in that practice understand that sometimes a ruptured appendix can damage those fibrae. Okay.",
          "start": "87.96",
          "words": [
            {
              "end": 88.06,
              "word": "No.",
              "start": 87.96
            },
            {
              "end": 88.74,
              "word": "No.",
              "start": 88.22
            },
            {
              "end": 88.86,
              "word": "The",
              "start": 88.74
            },
            {
              "end": 89.34,
              "word": "condition",
              "start": 88.86
            },
            {
              "end": 89.58,
              "word": "of",
              "start": 89.34
            },
            {
              "end": 89.64,
              "word": "her",
              "start": 89.58
            },
            {
              "end": 90.02,
              "word": "uterus",
              "start": 89.64
            },
            {
              "end": 90.22,
              "word": "is",
              "start": 90.02
            },
            {
              "end": 90.56,
              "word": "good.",
              "start": 90.22
            },
            {
              "end": 90.88,
              "word": "Her",
              "start": 90.64
            },
            {
              "end": 91.48,
              "word": "tubes,",
              "start": 90.88
            },
            {
              "end": 91.68,
              "word": "they",
              "start": 91.58
            },
            {
              "end": 91.88,
              "word": "did",
              "start": 91.68
            },
            {
              "end": 92.08,
              "word": "like",
              "start": 91.88
            },
            {
              "end": 92.18,
              "word": "an",
              "start": 92.08
            },
            {
              "end": 93.18,
              "word": "HSG",
              "start": 92.18
            },
            {
              "end": 93.74,
              "word": "and",
              "start": 93.18
            },
            {
              "end": 94.04,
              "word": "like",
              "start": 93.74
            },
            {
              "end": 94.2,
              "word": "the",
              "start": 94.04
            },
            {
              "end": 94.56,
              "word": "tubes",
              "start": 94.2
            },
            {
              "end": 94.84,
              "word": "are",
              "start": 94.56
            },
            {
              "end": 95.24,
              "word": "healthy.",
              "start": 94.84
            },
            {
              "end": 95.74,
              "word": "It's",
              "start": 95.36
            },
            {
              "end": 95.94,
              "word": "really",
              "start": 95.74
            },
            {
              "end": 96.3,
              "word": "like",
              "start": 95.94
            },
            {
              "end": 96.76,
              "word": "at",
              "start": 96.3
            },
            {
              "end": 96.94,
              "word": "the",
              "start": 96.76
            },
            {
              "end": 97.34,
              "word": "end",
              "start": 96.94
            },
            {
              "end": 97.5,
              "word": "of",
              "start": 97.34
            },
            {
              "end": 97.6,
              "word": "the",
              "start": 97.5
            },
            {
              "end": 98.02,
              "word": "tubes,",
              "start": 97.6
            },
            {
              "end": 98.44,
              "word": "there's",
              "start": 98.2
            },
            {
              "end": 98.56,
              "word": "like",
              "start": 98.44
            },
            {
              "end": 98.72,
              "word": "these",
              "start": 98.56
            },
            {
              "end": 98.94,
              "word": "little",
              "start": 98.72
            },
            {
              "end": 99.84,
              "word": "fibrae",
              "start": 98.94
            },
            {
              "end": 100.76,
              "word": "that",
              "start": 99.84
            },
            {
              "end": 101.6,
              "word": "need",
              "start": 100.76
            },
            {
              "end": 101.84,
              "word": "to",
              "start": 101.6
            },
            {
              "end": 102,
              "word": "be,",
              "start": 101.84
            },
            {
              "end": 103.08,
              "word": "they",
              "start": 102.18
            },
            {
              "end": 103.34,
              "word": "need,",
              "start": 103.08
            },
            {
              "end": 103.48,
              "word": "they",
              "start": 103.38
            },
            {
              "end": 103.78,
              "word": "perform",
              "start": 103.48
            },
            {
              "end": 104.12,
              "word": "this",
              "start": 103.78
            },
            {
              "end": 104.26,
              "word": "one",
              "start": 104.12
            },
            {
              "end": 104.78,
              "word": "task",
              "start": 104.26
            },
            {
              "end": 104.98,
              "word": "of",
              "start": 104.78
            },
            {
              "end": 105.3,
              "word": "basically",
              "start": 104.98
            },
            {
              "end": 105.72,
              "word": "like",
              "start": 105.3
            },
            {
              "end": 106.04,
              "word": "picking",
              "start": 105.72
            },
            {
              "end": 106.46,
              "word": "up",
              "start": 106.04
            },
            {
              "end": 107.02,
              "word": "the",
              "start": 106.46
            },
            {
              "end": 107.26,
              "word": "egg.",
              "start": 107.02
            },
            {
              "end": 107.58,
              "word": "Eggs,",
              "start": 107.28
            },
            {
              "end": 107.78,
              "word": "right.",
              "start": 107.58
            },
            {
              "end": 108.34,
              "word": "And",
              "start": 108.04
            },
            {
              "end": 108.46,
              "word": "he",
              "start": 108.34
            },
            {
              "end": 108.7,
              "word": "said",
              "start": 108.46
            },
            {
              "end": 108.88,
              "word": "that",
              "start": 108.7
            },
            {
              "end": 110.36,
              "word": "anecdotally,",
              "start": 108.88
            },
            {
              "end": 112.92,
              "word": "people",
              "start": 110.42
            },
            {
              "end": 113.34,
              "word": "in",
              "start": 112.92
            },
            {
              "end": 113.48,
              "word": "that",
              "start": 113.34
            },
            {
              "end": 113.98,
              "word": "practice",
              "start": 113.48
            },
            {
              "end": 114.48,
              "word": "understand",
              "start": 113.98
            },
            {
              "end": 114.82,
              "word": "that",
              "start": 114.48
            },
            {
              "end": 115.08,
              "word": "sometimes",
              "start": 114.82
            },
            {
              "end": 115.36,
              "word": "a",
              "start": 115.08
            },
            {
              "end": 115.7,
              "word": "ruptured",
              "start": 115.36
            },
            {
              "end": 116.14,
              "word": "appendix",
              "start": 115.7
            },
            {
              "end": 116.34,
              "word": "can",
              "start": 116.14
            },
            {
              "end": 116.82,
              "word": "damage",
              "start": 116.34
            },
            {
              "end": 117.16,
              "word": "those",
              "start": 116.82
            },
            {
              "end": 117.94,
              "word": "fibrae.",
              "start": 117.16
            },
            {
              "end": 118.68,
              "word": "Okay.",
              "start": 117.94
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "121.5",
          "text": "How long have you all been trying?",
          "start": "119.34",
          "words": [
            {
              "end": 119.82,
              "word": "How",
              "start": 119.34
            },
            {
              "end": 120.06,
              "word": "long",
              "start": 119.82
            },
            {
              "end": 120.18,
              "word": "have",
              "start": 120.06
            },
            {
              "end": 120.36,
              "word": "you",
              "start": 120.18
            },
            {
              "end": 120.56,
              "word": "all",
              "start": 120.36
            },
            {
              "end": 120.76,
              "word": "been",
              "start": 120.56
            },
            {
              "end": 121.5,
              "word": "trying?",
              "start": 120.76
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "122.96",
          "text": "For about one year.",
          "start": "121.8",
          "words": [
            {
              "end": 122.16,
              "word": "For",
              "start": 121.8
            },
            {
              "end": 122.38,
              "word": "about",
              "start": 122.16
            },
            {
              "end": 122.68,
              "word": "one",
              "start": 122.38
            },
            {
              "end": 122.96,
              "word": "year.",
              "start": 122.68
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "126.8",
          "text": "One year. Yeah. Okay. Okay. All right.",
          "start": "123.14",
          "words": [
            {
              "end": 123.62,
              "word": "One",
              "start": 123.14
            },
            {
              "end": 123.84,
              "word": "year.",
              "start": 123.62
            },
            {
              "end": 124.24,
              "word": "Yeah.",
              "start": 124.04
            },
            {
              "end": 124.84,
              "word": "Okay.",
              "start": 124.36
            },
            {
              "end": 125.58,
              "word": "Okay.",
              "start": 125.1
            },
            {
              "end": 126.6,
              "word": "All",
              "start": 126.12
            },
            {
              "end": 126.8,
              "word": "right.",
              "start": 126.6
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "147.66",
          "text": "So our age, we're 34. So his response to that was, you've been trying for one year, your age, your health, he said, I would assume you have a 4% chance of conceiving naturally. But because of this appendix thing, it's pretty much out of the picture.",
          "start": "127.18",
          "words": [
            {
              "end": 127.66,
              "word": "So",
              "start": 127.18
            },
            {
              "end": 128.36,
              "word": "our",
              "start": 127.66
            },
            {
              "end": 128.56,
              "word": "age,",
              "start": 128.36
            },
            {
              "end": 128.78,
              "word": "we're",
              "start": 128.6
            },
            {
              "end": 129.2,
              "word": "34.",
              "start": 128.78
            },
            {
              "end": 130.36,
              "word": "So",
              "start": 129.88
            },
            {
              "end": 130.78,
              "word": "his",
              "start": 130.36
            },
            {
              "end": 132.06,
              "word": "response",
              "start": 130.78
            },
            {
              "end": 132.44,
              "word": "to",
              "start": 132.06
            },
            {
              "end": 132.62,
              "word": "that",
              "start": 132.44
            },
            {
              "end": 133.12,
              "word": "was,",
              "start": 132.62
            },
            {
              "end": 134.52,
              "word": "you've",
              "start": 133.38
            },
            {
              "end": 134.6,
              "word": "been",
              "start": 134.52
            },
            {
              "end": 134.84,
              "word": "trying",
              "start": 134.6
            },
            {
              "end": 135.04,
              "word": "for",
              "start": 134.84
            },
            {
              "end": 135.24,
              "word": "one",
              "start": 135.04
            },
            {
              "end": 135.54,
              "word": "year,",
              "start": 135.24
            },
            {
              "end": 136.28,
              "word": "your",
              "start": 135.68
            },
            {
              "end": 136.66,
              "word": "age,",
              "start": 136.28
            },
            {
              "end": 136.96,
              "word": "your",
              "start": 136.8
            },
            {
              "end": 137.36,
              "word": "health,",
              "start": 136.96
            },
            {
              "end": 138.48,
              "word": "he",
              "start": 137.5
            },
            {
              "end": 138.68,
              "word": "said,",
              "start": 138.48
            },
            {
              "end": 139.74,
              "word": "I",
              "start": 139.26
            },
            {
              "end": 140,
              "word": "would",
              "start": 139.74
            },
            {
              "end": 140.22,
              "word": "assume",
              "start": 140
            },
            {
              "end": 140.44,
              "word": "you",
              "start": 140.22
            },
            {
              "end": 140.56,
              "word": "have",
              "start": 140.44
            },
            {
              "end": 140.68,
              "word": "a",
              "start": 140.56
            },
            {
              "end": 140.96,
              "word": "4",
              "start": 140.68
            },
            {
              "end": 141.32,
              "word": "%",
              "start": 140.96
            },
            {
              "end": 141.68,
              "word": "chance",
              "start": 141.32
            },
            {
              "end": 142.04,
              "word": "of",
              "start": 141.68
            },
            {
              "end": 142.52,
              "word": "conceiving",
              "start": 142.04
            },
            {
              "end": 142.92,
              "word": "naturally.",
              "start": 142.52
            },
            {
              "end": 143.94,
              "word": "But",
              "start": 143.46
            },
            {
              "end": 144.22,
              "word": "because",
              "start": 143.94
            },
            {
              "end": 144.44,
              "word": "of",
              "start": 144.22
            },
            {
              "end": 144.6,
              "word": "this",
              "start": 144.44
            },
            {
              "end": 145.14,
              "word": "appendix",
              "start": 144.6
            },
            {
              "end": 145.4,
              "word": "thing,",
              "start": 145.14
            },
            {
              "end": 146.6,
              "word": "it's",
              "start": 145.62
            },
            {
              "end": 146.76,
              "word": "pretty",
              "start": 146.6
            },
            {
              "end": 146.98,
              "word": "much",
              "start": 146.76
            },
            {
              "end": 147.18,
              "word": "out",
              "start": 146.98
            },
            {
              "end": 147.28,
              "word": "of",
              "start": 147.18
            },
            {
              "end": 147.34,
              "word": "the",
              "start": 147.28
            },
            {
              "end": 147.66,
              "word": "picture.",
              "start": 147.34
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "149.12",
          "text": "Oh, what?",
          "start": "147.66",
          "words": [
            {
              "end": 148.24,
              "word": "Oh,",
              "start": 147.66
            },
            {
              "end": 149.12,
              "word": "what?",
              "start": 148.46
            }
          ],
          "speaker": "SPEAKER_01"
        },
        {
          "end": "187.58",
          "text": "So this is, this is just kind of the way that, and he basically was like, okay, we just need to do some tests to understand if you guys are actually even a candidate for IVF. So that's what we've been proceeding on. I've told that to my mom, my mom had a career in healthcare and she's like delivered babies and things. And she was, she's generally pretty skeptical, but she was like, especially with fertility clinics. She said it would definitely be advantageous to have opinions from people who are not just in that practice. Yeah.",
          "start": "149.46",
          "words": [
            {
              "end": 149.94,
              "word": "So",
              "start": 149.46
            },
            {
              "end": 150.24,
              "word": "this",
              "start": 149.94
            },
            {
              "end": 150.52,
              "word": "is,",
              "start": 150.24
            },
            {
              "end": 150.78,
              "word": "this",
              "start": 150.52
            },
            {
              "end": 150.92,
              "word": "is",
              "start": 150.78
            },
            {
              "end": 151.28,
              "word": "just",
              "start": 150.92
            },
            {
              "end": 151.98,
              "word": "kind",
              "start": 151.28
            },
            {
              "end": 152.12,
              "word": "of",
              "start": 151.98
            },
            {
              "end": 152.22,
              "word": "the",
              "start": 152.12
            },
            {
              "end": 152.42,
              "word": "way",
              "start": 152.22
            },
            {
              "end": 152.56,
              "word": "that,",
              "start": 152.42
            },
            {
              "end": 152.68,
              "word": "and",
              "start": 152.58
            },
            {
              "end": 152.82,
              "word": "he",
              "start": 152.68
            },
            {
              "end": 153.16,
              "word": "basically",
              "start": 152.82
            },
            {
              "end": 153.38,
              "word": "was",
              "start": 153.16
            },
            {
              "end": 153.52,
              "word": "like,",
              "start": 153.38
            },
            {
              "end": 153.84,
              "word": "okay,",
              "start": 153.58
            },
            {
              "end": 154.36,
              "word": "we",
              "start": 153.84
            },
            {
              "end": 154.64,
              "word": "just",
              "start": 154.36
            },
            {
              "end": 154.78,
              "word": "need",
              "start": 154.64
            },
            {
              "end": 154.94,
              "word": "to",
              "start": 154.78
            },
            {
              "end": 155.04,
              "word": "do",
              "start": 154.94
            },
            {
              "end": 155.16,
              "word": "some",
              "start": 155.04
            },
            {
              "end": 155.5,
              "word": "tests",
              "start": 155.16
            },
            {
              "end": 155.68,
              "word": "to",
              "start": 155.5
            },
            {
              "end": 156.06,
              "word": "understand",
              "start": 155.68
            },
            {
              "end": 156.3,
              "word": "if",
              "start": 156.06
            },
            {
              "end": 156.38,
              "word": "you",
              "start": 156.3
            },
            {
              "end": 156.58,
              "word": "guys",
              "start": 156.38
            },
            {
              "end": 156.74,
              "word": "are",
              "start": 156.58
            },
            {
              "end": 157.04,
              "word": "actually",
              "start": 156.74
            },
            {
              "end": 157.28,
              "word": "even",
              "start": 157.04
            },
            {
              "end": 157.42,
              "word": "a",
              "start": 157.28
            },
            {
              "end": 157.76,
              "word": "candidate",
              "start": 157.42
            },
            {
              "end": 158.08,
              "word": "for",
              "start": 157.76
            },
            {
              "end": 158.68,
              "word": "IVF.",
              "start": 158.08
            },
            {
              "end": 159.5,
              "word": "So",
              "start": 158.98
            },
            {
              "end": 159.8,
              "word": "that's",
              "start": 159.5
            },
            {
              "end": 159.88,
              "word": "what",
              "start": 159.8
            },
            {
              "end": 160.1,
              "word": "we've",
              "start": 159.88
            },
            {
              "end": 160.24,
              "word": "been",
              "start": 160.1
            },
            {
              "end": 161.12,
              "word": "proceeding",
              "start": 160.24
            },
            {
              "end": 161.34,
              "word": "on.",
              "start": 161.12
            },
            {
              "end": 162.2,
              "word": "I've",
              "start": 161.68
            },
            {
              "end": 162.46,
              "word": "told",
              "start": 162.2
            },
            {
              "end": 162.88,
              "word": "that",
              "start": 162.46
            },
            {
              "end": 163.14,
              "word": "to",
              "start": 162.88
            },
            {
              "end": 163.28,
              "word": "my",
              "start": 163.14
            },
            {
              "end": 163.52,
              "word": "mom,",
              "start": 163.28
            },
            {
              "end": 163.68,
              "word": "my",
              "start": 163.58
            },
            {
              "end": 163.86,
              "word": "mom",
              "start": 163.68
            },
            {
              "end": 164.02,
              "word": "had",
              "start": 163.86
            },
            {
              "end": 164.12,
              "word": "a",
              "start": 164.02
            },
            {
              "end": 164.56,
              "word": "career",
              "start": 164.12
            },
            {
              "end": 164.74,
              "word": "in",
              "start": 164.56
            },
            {
              "end": 165.02,
              "word": "healthcare",
              "start": 164.74
            },
            {
              "end": 166.54,
              "word": "and",
              "start": 165.02
            },
            {
              "end": 168,
              "word": "she's",
              "start": 166.54
            },
            {
              "end": 168.1,
              "word": "like",
              "start": 168
            },
            {
              "end": 168.4,
              "word": "delivered",
              "start": 168.1
            },
            {
              "end": 168.82,
              "word": "babies",
              "start": 168.4
            },
            {
              "end": 169.02,
              "word": "and",
              "start": 168.82
            },
            {
              "end": 169.34,
              "word": "things.",
              "start": 169.02
            },
            {
              "end": 169.46,
              "word": "And",
              "start": 169.34
            },
            {
              "end": 170.44,
              "word": "she",
              "start": 169.46
            },
            {
              "end": 171.28,
              "word": "was,",
              "start": 170.44
            },
            {
              "end": 171.7,
              "word": "she's",
              "start": 171.32
            },
            {
              "end": 172.14,
              "word": "generally",
              "start": 171.7
            },
            {
              "end": 172.42,
              "word": "pretty",
              "start": 172.14
            },
            {
              "end": 172.98,
              "word": "skeptical,",
              "start": 172.42
            },
            {
              "end": 173.82,
              "word": "but",
              "start": 172.98
            },
            {
              "end": 174.08,
              "word": "she",
              "start": 173.82
            },
            {
              "end": 174.28,
              "word": "was",
              "start": 174.08
            },
            {
              "end": 174.6,
              "word": "like,",
              "start": 174.28
            },
            {
              "end": 175.38,
              "word": "especially",
              "start": 174.68
            },
            {
              "end": 175.94,
              "word": "with",
              "start": 175.38
            },
            {
              "end": 176.32,
              "word": "fertility",
              "start": 175.94
            },
            {
              "end": 176.82,
              "word": "clinics.",
              "start": 176.32
            },
            {
              "end": 177.66,
              "word": "She",
              "start": 177.66
            },
            {
              "end": 177.8,
              "word": "said",
              "start": 177.66
            },
            {
              "end": 177.96,
              "word": "it",
              "start": 177.8
            },
            {
              "end": 178.1,
              "word": "would",
              "start": 177.96
            },
            {
              "end": 178.78,
              "word": "definitely",
              "start": 178.1
            },
            {
              "end": 179.62,
              "word": "be",
              "start": 178.78
            },
            {
              "end": 180.7,
              "word": "advantageous",
              "start": 179.62
            },
            {
              "end": 180.94,
              "word": "to",
              "start": 180.7
            },
            {
              "end": 181.22,
              "word": "have",
              "start": 180.94
            },
            {
              "end": 182.62,
              "word": "opinions",
              "start": 181.22
            },
            {
              "end": 182.98,
              "word": "from",
              "start": 182.62
            },
            {
              "end": 183.38,
              "word": "people",
              "start": 182.98
            },
            {
              "end": 184.44,
              "word": "who",
              "start": 183.38
            },
            {
              "end": 184.7,
              "word": "are",
              "start": 184.44
            },
            {
              "end": 185.06,
              "word": "not",
              "start": 184.7
            },
            {
              "end": 186.12,
              "word": "just",
              "start": 185.06
            },
            {
              "end": 186.3,
              "word": "in",
              "start": 186.12
            },
            {
              "end": 186.42,
              "word": "that",
              "start": 186.3
            },
            {
              "end": 186.84,
              "word": "practice.",
              "start": 186.42
            },
            {
              "end": 187.58,
              "word": "Yeah.",
              "start": 187.1
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "189.0",
          "text": "Yeah. Sorry.",
          "start": "187.9",
          "words": [
            {
              "end": 188.5,
              "word": "Yeah.",
              "start": 187.9
            },
            {
              "end": 189,
              "word": "Sorry.",
              "start": 188.68
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "191.76",
          "text": "Does that, does that give you a picture? Right.",
          "start": "189.08",
          "words": [
            {
              "end": 189.6,
              "word": "Does",
              "start": 189.08
            },
            {
              "end": 189.86,
              "word": "that,",
              "start": 189.6
            },
            {
              "end": 190.32,
              "word": "does",
              "start": 189.86
            },
            {
              "end": 190.46,
              "word": "that",
              "start": 190.32
            },
            {
              "end": 190.62,
              "word": "give",
              "start": 190.46
            },
            {
              "end": 190.78,
              "word": "you",
              "start": 190.62
            },
            {
              "end": 190.86,
              "word": "a",
              "start": 190.78
            },
            {
              "end": 191.16,
              "word": "picture?",
              "start": 190.86
            },
            {
              "end": 191.76,
              "word": "Right.",
              "start": 191.28
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "213.84",
          "text": "Right. Cause we were wondering about like, what's the whole issue with fertility? Um, cause we're not getting like enough information for us to get an idea of what's going on with you and your partner for us to be able to make. Uh, an educative, um, or agentive care for you. So what is your goal with us?",
          "start": "192.0",
          "words": [
            {
              "end": 192.4,
              "word": "Right.",
              "start": 192
            },
            {
              "end": 192.94,
              "word": "Cause",
              "start": 192.6
            },
            {
              "end": 193.26,
              "word": "we",
              "start": 192.94
            },
            {
              "end": 193.4,
              "word": "were",
              "start": 193.26
            },
            {
              "end": 193.82,
              "word": "wondering",
              "start": 193.4
            },
            {
              "end": 194.48,
              "word": "about",
              "start": 193.82
            },
            {
              "end": 194.78,
              "word": "like,",
              "start": 194.48
            },
            {
              "end": 195.18,
              "word": "what's",
              "start": 194.86
            },
            {
              "end": 195.28,
              "word": "the",
              "start": 195.18
            },
            {
              "end": 195.54,
              "word": "whole",
              "start": 195.28
            },
            {
              "end": 196,
              "word": "issue",
              "start": 195.54
            },
            {
              "end": 196.3,
              "word": "with",
              "start": 196
            },
            {
              "end": 196.84,
              "word": "fertility?",
              "start": 196.3
            },
            {
              "end": 197.7,
              "word": "Um,",
              "start": 197.18
            },
            {
              "end": 198.42,
              "word": "cause",
              "start": 198
            },
            {
              "end": 198.66,
              "word": "we're",
              "start": 198.42
            },
            {
              "end": 198.8,
              "word": "not",
              "start": 198.66
            },
            {
              "end": 199.1,
              "word": "getting",
              "start": 198.8
            },
            {
              "end": 199.3,
              "word": "like",
              "start": 199.1
            },
            {
              "end": 199.56,
              "word": "enough",
              "start": 199.3
            },
            {
              "end": 200.06,
              "word": "information",
              "start": 199.56
            },
            {
              "end": 200.36,
              "word": "for",
              "start": 200.06
            },
            {
              "end": 200.54,
              "word": "us",
              "start": 200.36
            },
            {
              "end": 200.82,
              "word": "to",
              "start": 200.54
            },
            {
              "end": 201.6,
              "word": "get",
              "start": 200.82
            },
            {
              "end": 201.8,
              "word": "an",
              "start": 201.6
            },
            {
              "end": 202.18,
              "word": "idea",
              "start": 201.8
            },
            {
              "end": 202.34,
              "word": "of",
              "start": 202.18
            },
            {
              "end": 202.68,
              "word": "what's",
              "start": 202.34
            },
            {
              "end": 202.9,
              "word": "going",
              "start": 202.68
            },
            {
              "end": 203.22,
              "word": "on",
              "start": 202.9
            },
            {
              "end": 203.46,
              "word": "with",
              "start": 203.22
            },
            {
              "end": 203.76,
              "word": "you",
              "start": 203.46
            },
            {
              "end": 204.02,
              "word": "and",
              "start": 203.76
            },
            {
              "end": 204.14,
              "word": "your",
              "start": 204.02
            },
            {
              "end": 204.5,
              "word": "partner",
              "start": 204.14
            },
            {
              "end": 205.32,
              "word": "for",
              "start": 204.5
            },
            {
              "end": 205.5,
              "word": "us",
              "start": 205.32
            },
            {
              "end": 205.74,
              "word": "to",
              "start": 205.5
            },
            {
              "end": 206.18,
              "word": "be",
              "start": 205.74
            },
            {
              "end": 206.4,
              "word": "able",
              "start": 206.18
            },
            {
              "end": 206.62,
              "word": "to",
              "start": 206.4
            },
            {
              "end": 206.94,
              "word": "make.",
              "start": 206.62
            },
            {
              "end": 207.28,
              "word": "Uh,",
              "start": 206.94
            },
            {
              "end": 208.14,
              "word": "an",
              "start": 207.58
            },
            {
              "end": 208.94,
              "word": "educative,",
              "start": 208.14
            },
            {
              "end": 209.72,
              "word": "um,",
              "start": 209.1
            },
            {
              "end": 210.18,
              "word": "or",
              "start": 209.92
            },
            {
              "end": 210.82,
              "word": "agentive",
              "start": 210.18
            },
            {
              "end": 211.08,
              "word": "care",
              "start": 210.82
            },
            {
              "end": 211.32,
              "word": "for",
              "start": 211.08
            },
            {
              "end": 211.62,
              "word": "you.",
              "start": 211.32
            },
            {
              "end": 212.4,
              "word": "So",
              "start": 211.9
            },
            {
              "end": 212.68,
              "word": "what",
              "start": 212.4
            },
            {
              "end": 212.82,
              "word": "is",
              "start": 212.68
            },
            {
              "end": 213.04,
              "word": "your",
              "start": 212.82
            },
            {
              "end": 213.36,
              "word": "goal",
              "start": 213.04
            },
            {
              "end": 213.6,
              "word": "with",
              "start": 213.36
            },
            {
              "end": 213.84,
              "word": "us?",
              "start": 213.6
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "276.16",
          "text": "Oh, it was simply, I asked the previous practitioner that I spoke with, I said, Hey, I'm, I have the, you guys are technically my primary care practitioners. So I said, Hey, look, I have this issue that I'm discussing with a specialist, a fertility clinic. Yeah. I'm wondering, could I, when I have those results, could I present them to you for just another opinion? Obviously you're not a fertility clinic, there's going to be limited, but it could be, Oh, everything looks totally normal and fine and within range on your semen analysis. So we don't have further input here, maybe some studies that have indicated that it's good for men to not drink, you know, in six months prior to conception, whatever, you know, just kind of general suggestions or perhaps the sperm count is low. And. Yeah. So again, perhaps there are some suggestions. It's hard to say anything right now because you obviously I haven't presented with you with any labs. Yeah.",
          "start": "214.86",
          "words": [
            {
              "end": 215.36,
              "word": "Oh,",
              "start": 214.86
            },
            {
              "end": 215.7,
              "word": "it",
              "start": 215.52
            },
            {
              "end": 215.86,
              "word": "was",
              "start": 215.7
            },
            {
              "end": 216.2,
              "word": "simply,",
              "start": 215.86
            },
            {
              "end": 216.48,
              "word": "I",
              "start": 216.26
            },
            {
              "end": 216.8,
              "word": "asked",
              "start": 216.48
            },
            {
              "end": 216.96,
              "word": "the",
              "start": 216.8
            },
            {
              "end": 217.3,
              "word": "previous",
              "start": 216.96
            },
            {
              "end": 217.76,
              "word": "practitioner",
              "start": 217.3
            },
            {
              "end": 218.12,
              "word": "that",
              "start": 217.76
            },
            {
              "end": 218.2,
              "word": "I",
              "start": 218.12
            },
            {
              "end": 218.4,
              "word": "spoke",
              "start": 218.2
            },
            {
              "end": 218.7,
              "word": "with,",
              "start": 218.4
            },
            {
              "end": 218.86,
              "word": "I",
              "start": 218.76
            },
            {
              "end": 219.12,
              "word": "said,",
              "start": 218.86
            },
            {
              "end": 219.38,
              "word": "Hey,",
              "start": 219.12
            },
            {
              "end": 220.18,
              "word": "I'm,",
              "start": 219.4
            },
            {
              "end": 220.44,
              "word": "I",
              "start": 220.24
            },
            {
              "end": 220.82,
              "word": "have",
              "start": 220.44
            },
            {
              "end": 220.94,
              "word": "the,",
              "start": 220.82
            },
            {
              "end": 221.16,
              "word": "you",
              "start": 221
            },
            {
              "end": 221.36,
              "word": "guys",
              "start": 221.16
            },
            {
              "end": 221.52,
              "word": "are",
              "start": 221.36
            },
            {
              "end": 221.86,
              "word": "technically",
              "start": 221.52
            },
            {
              "end": 222.16,
              "word": "my",
              "start": 221.86
            },
            {
              "end": 222.6,
              "word": "primary",
              "start": 222.16
            },
            {
              "end": 222.86,
              "word": "care",
              "start": 222.6
            },
            {
              "end": 223.62,
              "word": "practitioners.",
              "start": 222.86
            },
            {
              "end": 224.12,
              "word": "So",
              "start": 223.8
            },
            {
              "end": 224.22,
              "word": "I",
              "start": 224.12
            },
            {
              "end": 224.88,
              "word": "said,",
              "start": 224.22
            },
            {
              "end": 225.08,
              "word": "Hey,",
              "start": 224.92
            },
            {
              "end": 225.26,
              "word": "look,",
              "start": 225.1
            },
            {
              "end": 225.66,
              "word": "I",
              "start": 225.38
            },
            {
              "end": 225.86,
              "word": "have",
              "start": 225.66
            },
            {
              "end": 226.04,
              "word": "this",
              "start": 225.86
            },
            {
              "end": 226.3,
              "word": "issue",
              "start": 226.04
            },
            {
              "end": 226.52,
              "word": "that",
              "start": 226.3
            },
            {
              "end": 226.66,
              "word": "I'm",
              "start": 226.52
            },
            {
              "end": 227.04,
              "word": "discussing",
              "start": 226.66
            },
            {
              "end": 227.36,
              "word": "with",
              "start": 227.04
            },
            {
              "end": 227.48,
              "word": "a",
              "start": 227.36
            },
            {
              "end": 227.96,
              "word": "specialist,",
              "start": 227.48
            },
            {
              "end": 228.22,
              "word": "a",
              "start": 228.04
            },
            {
              "end": 228.52,
              "word": "fertility",
              "start": 228.22
            },
            {
              "end": 229,
              "word": "clinic.",
              "start": 228.52
            },
            {
              "end": 229.44,
              "word": "Yeah.",
              "start": 229.12
            },
            {
              "end": 229.76,
              "word": "I'm",
              "start": 229.52
            },
            {
              "end": 230.2,
              "word": "wondering,",
              "start": 229.76
            },
            {
              "end": 230.94,
              "word": "could",
              "start": 230.28
            },
            {
              "end": 231.34,
              "word": "I,",
              "start": 230.94
            },
            {
              "end": 232,
              "word": "when",
              "start": 231.52
            },
            {
              "end": 232.2,
              "word": "I",
              "start": 232
            },
            {
              "end": 232.44,
              "word": "have",
              "start": 232.2
            },
            {
              "end": 232.7,
              "word": "those",
              "start": 232.44
            },
            {
              "end": 233.06,
              "word": "results,",
              "start": 232.7
            },
            {
              "end": 233.46,
              "word": "could",
              "start": 233.2
            },
            {
              "end": 233.8,
              "word": "I",
              "start": 233.46
            },
            {
              "end": 234.22,
              "word": "present",
              "start": 233.8
            },
            {
              "end": 234.44,
              "word": "them",
              "start": 234.22
            },
            {
              "end": 234.62,
              "word": "to",
              "start": 234.44
            },
            {
              "end": 234.82,
              "word": "you",
              "start": 234.62
            },
            {
              "end": 235.28,
              "word": "for",
              "start": 234.82
            },
            {
              "end": 235.56,
              "word": "just",
              "start": 235.28
            },
            {
              "end": 236.18,
              "word": "another",
              "start": 235.56
            },
            {
              "end": 236.84,
              "word": "opinion?",
              "start": 236.18
            },
            {
              "end": 237.58,
              "word": "Obviously",
              "start": 236.94
            },
            {
              "end": 238.12,
              "word": "you're",
              "start": 237.58
            },
            {
              "end": 238.26,
              "word": "not",
              "start": 238.12
            },
            {
              "end": 238.4,
              "word": "a",
              "start": 238.26
            },
            {
              "end": 238.72,
              "word": "fertility",
              "start": 238.4
            },
            {
              "end": 239.16,
              "word": "clinic,",
              "start": 238.72
            },
            {
              "end": 239.72,
              "word": "there's",
              "start": 239.36
            },
            {
              "end": 239.82,
              "word": "going",
              "start": 239.72
            },
            {
              "end": 239.92,
              "word": "to",
              "start": 239.82
            },
            {
              "end": 240.06,
              "word": "be",
              "start": 239.92
            },
            {
              "end": 240.48,
              "word": "limited,",
              "start": 240.06
            },
            {
              "end": 241.18,
              "word": "but",
              "start": 240.66
            },
            {
              "end": 241.34,
              "word": "it",
              "start": 241.18
            },
            {
              "end": 241.54,
              "word": "could",
              "start": 241.34
            },
            {
              "end": 241.92,
              "word": "be,",
              "start": 241.54
            },
            {
              "end": 243.14,
              "word": "Oh,",
              "start": 242.08
            },
            {
              "end": 243.48,
              "word": "everything",
              "start": 243.24
            },
            {
              "end": 243.94,
              "word": "looks",
              "start": 243.48
            },
            {
              "end": 244.54,
              "word": "totally",
              "start": 243.94
            },
            {
              "end": 245,
              "word": "normal",
              "start": 244.54
            },
            {
              "end": 245.22,
              "word": "and",
              "start": 245
            },
            {
              "end": 245.52,
              "word": "fine",
              "start": 245.22
            },
            {
              "end": 245.7,
              "word": "and",
              "start": 245.52
            },
            {
              "end": 245.84,
              "word": "within",
              "start": 245.7
            },
            {
              "end": 246.24,
              "word": "range",
              "start": 245.84
            },
            {
              "end": 246.4,
              "word": "on",
              "start": 246.24
            },
            {
              "end": 246.58,
              "word": "your",
              "start": 246.4
            },
            {
              "end": 247.22,
              "word": "semen",
              "start": 246.58
            },
            {
              "end": 247.62,
              "word": "analysis.",
              "start": 247.22
            },
            {
              "end": 248.2,
              "word": "So",
              "start": 247.76
            },
            {
              "end": 248.46,
              "word": "we",
              "start": 248.2
            },
            {
              "end": 249.04,
              "word": "don't",
              "start": 248.46
            },
            {
              "end": 249.12,
              "word": "have",
              "start": 249.04
            },
            {
              "end": 249.38,
              "word": "further",
              "start": 249.12
            },
            {
              "end": 249.7,
              "word": "input",
              "start": 249.38
            },
            {
              "end": 250.72,
              "word": "here,",
              "start": 249.7
            },
            {
              "end": 251.12,
              "word": "maybe",
              "start": 250.82
            },
            {
              "end": 251.42,
              "word": "some",
              "start": 251.12
            },
            {
              "end": 252.16,
              "word": "studies",
              "start": 251.42
            },
            {
              "end": 252.52,
              "word": "that",
              "start": 252.16
            },
            {
              "end": 252.66,
              "word": "have",
              "start": 252.52
            },
            {
              "end": 253.22,
              "word": "indicated",
              "start": 252.66
            },
            {
              "end": 253.64,
              "word": "that",
              "start": 253.22
            },
            {
              "end": 254.4,
              "word": "it's",
              "start": 253.64
            },
            {
              "end": 254.52,
              "word": "good",
              "start": 254.4
            },
            {
              "end": 254.76,
              "word": "for",
              "start": 254.52
            },
            {
              "end": 254.96,
              "word": "men",
              "start": 254.76
            },
            {
              "end": 255.32,
              "word": "to",
              "start": 254.96
            },
            {
              "end": 255.52,
              "word": "not",
              "start": 255.32
            },
            {
              "end": 256,
              "word": "drink,",
              "start": 255.52
            },
            {
              "end": 256.7,
              "word": "you",
              "start": 256.04
            },
            {
              "end": 256.92,
              "word": "know,",
              "start": 256.7
            },
            {
              "end": 257.64,
              "word": "in",
              "start": 256.92
            },
            {
              "end": 257.94,
              "word": "six",
              "start": 257.64
            },
            {
              "end": 258.28,
              "word": "months",
              "start": 257.94
            },
            {
              "end": 258.86,
              "word": "prior",
              "start": 258.28
            },
            {
              "end": 259.06,
              "word": "to",
              "start": 258.86
            },
            {
              "end": 259.32,
              "word": "conception,",
              "start": 259.06
            },
            {
              "end": 259.64,
              "word": "whatever,",
              "start": 259.38
            },
            {
              "end": 260.08,
              "word": "you",
              "start": 259.94
            },
            {
              "end": 260.22,
              "word": "know,",
              "start": 260.08
            },
            {
              "end": 260.34,
              "word": "just",
              "start": 260.22
            },
            {
              "end": 260.54,
              "word": "kind",
              "start": 260.34
            },
            {
              "end": 260.66,
              "word": "of",
              "start": 260.54
            },
            {
              "end": 261.12,
              "word": "general",
              "start": 260.66
            },
            {
              "end": 261.64,
              "word": "suggestions",
              "start": 261.12
            },
            {
              "end": 262.68,
              "word": "or",
              "start": 261.64
            },
            {
              "end": 263.06,
              "word": "perhaps",
              "start": 262.68
            },
            {
              "end": 263.34,
              "word": "the",
              "start": 263.06
            },
            {
              "end": 263.54,
              "word": "sperm",
              "start": 263.34
            },
            {
              "end": 263.86,
              "word": "count",
              "start": 263.54
            },
            {
              "end": 264.08,
              "word": "is",
              "start": 263.86
            },
            {
              "end": 264.42,
              "word": "low.",
              "start": 264.08
            },
            {
              "end": 265.18,
              "word": "And.",
              "start": 264.62
            },
            {
              "end": 266.38,
              "word": "Yeah.",
              "start": 265.82
            },
            {
              "end": 266.38,
              "word": "So",
              "start": 266.38
            },
            {
              "end": 266.38,
              "word": "again,",
              "start": 266.38
            },
            {
              "end": 266.8,
              "word": "perhaps",
              "start": 266.5
            },
            {
              "end": 267.28,
              "word": "there",
              "start": 266.8
            },
            {
              "end": 267.4,
              "word": "are",
              "start": 267.28
            },
            {
              "end": 267.6,
              "word": "some",
              "start": 267.4
            },
            {
              "end": 268.2,
              "word": "suggestions.",
              "start": 267.6
            },
            {
              "end": 270.5,
              "word": "It's",
              "start": 270.06
            },
            {
              "end": 270.86,
              "word": "hard",
              "start": 270.5
            },
            {
              "end": 271.02,
              "word": "to",
              "start": 270.86
            },
            {
              "end": 271.22,
              "word": "say",
              "start": 271.02
            },
            {
              "end": 271.44,
              "word": "anything",
              "start": 271.22
            },
            {
              "end": 271.66,
              "word": "right",
              "start": 271.44
            },
            {
              "end": 271.84,
              "word": "now",
              "start": 271.66
            },
            {
              "end": 272.04,
              "word": "because",
              "start": 271.84
            },
            {
              "end": 272.22,
              "word": "you",
              "start": 272.04
            },
            {
              "end": 273.32,
              "word": "obviously",
              "start": 272.22
            },
            {
              "end": 273.98,
              "word": "I",
              "start": 273.32
            },
            {
              "end": 274.26,
              "word": "haven't",
              "start": 273.98
            },
            {
              "end": 274.54,
              "word": "presented",
              "start": 274.26
            },
            {
              "end": 274.92,
              "word": "with",
              "start": 274.54
            },
            {
              "end": 275.1,
              "word": "you",
              "start": 274.92
            },
            {
              "end": 275.2,
              "word": "with",
              "start": 275.1
            },
            {
              "end": 275.42,
              "word": "any",
              "start": 275.2
            },
            {
              "end": 275.74,
              "word": "labs.",
              "start": 275.42
            },
            {
              "end": 276.16,
              "word": "Yeah.",
              "start": 275.94
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "284.24",
          "text": "Okay. Um, it's your, your wife, right? Right. Is she able to come in as well?",
          "start": "277.16",
          "words": [
            {
              "end": 277.6,
              "word": "Okay.",
              "start": 277.16
            },
            {
              "end": 278.36,
              "word": "Um,",
              "start": 277.92
            },
            {
              "end": 279.86,
              "word": "it's",
              "start": 278.58
            },
            {
              "end": 280.02,
              "word": "your,",
              "start": 279.86
            },
            {
              "end": 280.98,
              "word": "your",
              "start": 280.22
            },
            {
              "end": 281.32,
              "word": "wife,",
              "start": 280.98
            },
            {
              "end": 281.62,
              "word": "right?",
              "start": 281.44
            },
            {
              "end": 282.1,
              "word": "Right.",
              "start": 281.7
            },
            {
              "end": 282.76,
              "word": "Is",
              "start": 282.32
            },
            {
              "end": 282.94,
              "word": "she",
              "start": 282.76
            },
            {
              "end": 283.12,
              "word": "able",
              "start": 282.94
            },
            {
              "end": 283.3,
              "word": "to",
              "start": 283.12
            },
            {
              "end": 283.54,
              "word": "come",
              "start": 283.3
            },
            {
              "end": 283.78,
              "word": "in",
              "start": 283.54
            },
            {
              "end": 284.02,
              "word": "as",
              "start": 283.78
            },
            {
              "end": 284.24,
              "word": "well?",
              "start": 284.02
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "286.92",
          "text": "She could. Yeah. Yeah.",
          "start": "285.02",
          "words": [
            {
              "end": 285.46,
              "word": "She",
              "start": 285.02
            },
            {
              "end": 285.7,
              "word": "could.",
              "start": 285.46
            },
            {
              "end": 286.26,
              "word": "Yeah.",
              "start": 285.92
            },
            {
              "end": 286.92,
              "word": "Yeah.",
              "start": 286.48
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "311.8",
          "text": "Cause I think it would be better if two of you could come in once you guys get the results and bring everything in. So. Yeah. So she can have like a full idea of what's going on. Cause if we need to treat you or give you some sort of recommendation, she might also benefit from those stuff since it's both of you that produce the child, not just one person. This is true.",
          "start": "287.02",
          "words": [
            {
              "end": 287.16,
              "word": "Cause",
              "start": 287.02
            },
            {
              "end": 287.32,
              "word": "I",
              "start": 287.16
            },
            {
              "end": 287.48,
              "word": "think",
              "start": 287.32
            },
            {
              "end": 287.62,
              "word": "it",
              "start": 287.48
            },
            {
              "end": 287.7,
              "word": "would",
              "start": 287.62
            },
            {
              "end": 287.9,
              "word": "be",
              "start": 287.7
            },
            {
              "end": 288.18,
              "word": "better",
              "start": 287.9
            },
            {
              "end": 288.5,
              "word": "if",
              "start": 288.18
            },
            {
              "end": 288.78,
              "word": "two",
              "start": 288.5
            },
            {
              "end": 288.94,
              "word": "of",
              "start": 288.78
            },
            {
              "end": 289.2,
              "word": "you",
              "start": 288.94
            },
            {
              "end": 289.94,
              "word": "could",
              "start": 289.2
            },
            {
              "end": 290.22,
              "word": "come",
              "start": 289.94
            },
            {
              "end": 290.6,
              "word": "in",
              "start": 290.22
            },
            {
              "end": 292.06,
              "word": "once",
              "start": 290.6
            },
            {
              "end": 292.22,
              "word": "you",
              "start": 292.06
            },
            {
              "end": 292.44,
              "word": "guys",
              "start": 292.22
            },
            {
              "end": 292.88,
              "word": "get",
              "start": 292.44
            },
            {
              "end": 293.02,
              "word": "the",
              "start": 292.88
            },
            {
              "end": 293.42,
              "word": "results",
              "start": 293.02
            },
            {
              "end": 294.26,
              "word": "and",
              "start": 294.04
            },
            {
              "end": 294.46,
              "word": "bring",
              "start": 294.26
            },
            {
              "end": 294.96,
              "word": "everything",
              "start": 294.46
            },
            {
              "end": 295.4,
              "word": "in.",
              "start": 294.96
            },
            {
              "end": 295.7,
              "word": "So.",
              "start": 295.5
            },
            {
              "end": 296.5,
              "word": "Yeah.",
              "start": 296.38
            },
            {
              "end": 296.5,
              "word": "So",
              "start": 296.5
            },
            {
              "end": 296.5,
              "word": "she",
              "start": 296.5
            },
            {
              "end": 296.5,
              "word": "can",
              "start": 296.5
            },
            {
              "end": 296.5,
              "word": "have",
              "start": 296.5
            },
            {
              "end": 296.5,
              "word": "like",
              "start": 296.5
            },
            {
              "end": 296.5,
              "word": "a",
              "start": 296.5
            },
            {
              "end": 296.84,
              "word": "full",
              "start": 296.5
            },
            {
              "end": 297.34,
              "word": "idea",
              "start": 296.84
            },
            {
              "end": 298.48,
              "word": "of",
              "start": 297.34
            },
            {
              "end": 298.84,
              "word": "what's",
              "start": 298.48
            },
            {
              "end": 299,
              "word": "going",
              "start": 298.84
            },
            {
              "end": 299.3,
              "word": "on.",
              "start": 299
            },
            {
              "end": 299.66,
              "word": "Cause",
              "start": 299.44
            },
            {
              "end": 300.02,
              "word": "if",
              "start": 299.66
            },
            {
              "end": 300.7,
              "word": "we",
              "start": 300.02
            },
            {
              "end": 300.92,
              "word": "need",
              "start": 300.7
            },
            {
              "end": 301.1,
              "word": "to",
              "start": 300.92
            },
            {
              "end": 301.28,
              "word": "treat",
              "start": 301.1
            },
            {
              "end": 301.66,
              "word": "you",
              "start": 301.28
            },
            {
              "end": 302.08,
              "word": "or",
              "start": 301.66
            },
            {
              "end": 302.38,
              "word": "give",
              "start": 302.08
            },
            {
              "end": 302.6,
              "word": "you",
              "start": 302.38
            },
            {
              "end": 302.84,
              "word": "some",
              "start": 302.6
            },
            {
              "end": 303.06,
              "word": "sort",
              "start": 302.84
            },
            {
              "end": 303.28,
              "word": "of",
              "start": 303.06
            },
            {
              "end": 303.7,
              "word": "recommendation,",
              "start": 303.28
            },
            {
              "end": 304.22,
              "word": "she",
              "start": 304.1
            },
            {
              "end": 304.4,
              "word": "might",
              "start": 304.22
            },
            {
              "end": 304.72,
              "word": "also",
              "start": 304.4
            },
            {
              "end": 305.02,
              "word": "benefit",
              "start": 304.72
            },
            {
              "end": 305.72,
              "word": "from",
              "start": 305.02
            },
            {
              "end": 306.76,
              "word": "those",
              "start": 305.72
            },
            {
              "end": 307.18,
              "word": "stuff",
              "start": 306.76
            },
            {
              "end": 307.4,
              "word": "since",
              "start": 307.18
            },
            {
              "end": 307.7,
              "word": "it's",
              "start": 307.4
            },
            {
              "end": 308.12,
              "word": "both",
              "start": 307.7
            },
            {
              "end": 308.32,
              "word": "of",
              "start": 308.12
            },
            {
              "end": 308.56,
              "word": "you",
              "start": 308.32
            },
            {
              "end": 308.7,
              "word": "that",
              "start": 308.56
            },
            {
              "end": 309,
              "word": "produce",
              "start": 308.7
            },
            {
              "end": 309.2,
              "word": "the",
              "start": 309
            },
            {
              "end": 309.4,
              "word": "child,",
              "start": 309.2
            },
            {
              "end": 309.76,
              "word": "not",
              "start": 309.52
            },
            {
              "end": 310,
              "word": "just",
              "start": 309.76
            },
            {
              "end": 310.22,
              "word": "one",
              "start": 310
            },
            {
              "end": 310.52,
              "word": "person.",
              "start": 310.22
            },
            {
              "end": 311.34,
              "word": "This",
              "start": 310.86
            },
            {
              "end": 311.58,
              "word": "is",
              "start": 311.34
            },
            {
              "end": 311.8,
              "word": "true.",
              "start": 311.58
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "320.98",
          "text": "Okay, cool. So the right thing would be just wait until those labs are, and they should be all coming available here in the next couple of days. Yeah. Yeah.",
          "start": "311.98",
          "words": [
            {
              "end": 312.32,
              "word": "Okay,",
              "start": 311.98
            },
            {
              "end": 312.78,
              "word": "cool.",
              "start": 312.42
            },
            {
              "end": 313.16,
              "word": "So",
              "start": 312.88
            },
            {
              "end": 313.3,
              "word": "the",
              "start": 313.16
            },
            {
              "end": 313.48,
              "word": "right",
              "start": 313.3
            },
            {
              "end": 313.72,
              "word": "thing",
              "start": 313.48
            },
            {
              "end": 313.84,
              "word": "would",
              "start": 313.72
            },
            {
              "end": 313.96,
              "word": "be",
              "start": 313.84
            },
            {
              "end": 314.16,
              "word": "just",
              "start": 313.96
            },
            {
              "end": 314.62,
              "word": "wait",
              "start": 314.16
            },
            {
              "end": 314.9,
              "word": "until",
              "start": 314.62
            },
            {
              "end": 315.3,
              "word": "those",
              "start": 314.9
            },
            {
              "end": 315.78,
              "word": "labs",
              "start": 315.3
            },
            {
              "end": 316.1,
              "word": "are,",
              "start": 315.78
            },
            {
              "end": 316.32,
              "word": "and",
              "start": 316.2
            },
            {
              "end": 316.42,
              "word": "they",
              "start": 316.32
            },
            {
              "end": 316.62,
              "word": "should",
              "start": 316.42
            },
            {
              "end": 316.78,
              "word": "be",
              "start": 316.62
            },
            {
              "end": 316.98,
              "word": "all",
              "start": 316.78
            },
            {
              "end": 317.24,
              "word": "coming",
              "start": 316.98
            },
            {
              "end": 317.66,
              "word": "available",
              "start": 317.24
            },
            {
              "end": 317.98,
              "word": "here",
              "start": 317.66
            },
            {
              "end": 318.08,
              "word": "in",
              "start": 317.98
            },
            {
              "end": 318.16,
              "word": "the",
              "start": 318.08
            },
            {
              "end": 318.32,
              "word": "next",
              "start": 318.16
            },
            {
              "end": 318.56,
              "word": "couple",
              "start": 318.32
            },
            {
              "end": 318.64,
              "word": "of",
              "start": 318.56
            },
            {
              "end": 318.9,
              "word": "days.",
              "start": 318.64
            },
            {
              "end": 320.44,
              "word": "Yeah.",
              "start": 319.96
            },
            {
              "end": 320.98,
              "word": "Yeah.",
              "start": 320.54
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "334.68",
          "text": "So once you have the results and then she can also bring whatever workup that she needs. Yeah. So that's a great way for us to get this done already. Um, so that together we can look at like what might be going on with her. Great.",
          "start": "321.08",
          "words": [
            {
              "end": 321.3,
              "word": "So",
              "start": 321.08
            },
            {
              "end": 321.64,
              "word": "once",
              "start": 321.3
            },
            {
              "end": 321.98,
              "word": "you",
              "start": 321.64
            },
            {
              "end": 322.18,
              "word": "have",
              "start": 321.98
            },
            {
              "end": 322.28,
              "word": "the",
              "start": 322.18
            },
            {
              "end": 322.56,
              "word": "results",
              "start": 322.28
            },
            {
              "end": 322.98,
              "word": "and",
              "start": 322.56
            },
            {
              "end": 323.18,
              "word": "then",
              "start": 322.98
            },
            {
              "end": 323.48,
              "word": "she",
              "start": 323.18
            },
            {
              "end": 323.66,
              "word": "can",
              "start": 323.48
            },
            {
              "end": 323.96,
              "word": "also",
              "start": 323.66
            },
            {
              "end": 324.22,
              "word": "bring",
              "start": 323.96
            },
            {
              "end": 324.62,
              "word": "whatever",
              "start": 324.22
            },
            {
              "end": 325.16,
              "word": "workup",
              "start": 324.62
            },
            {
              "end": 325.42,
              "word": "that",
              "start": 325.16
            },
            {
              "end": 326.24,
              "word": "she",
              "start": 325.42
            },
            {
              "end": 326.36,
              "word": "needs.",
              "start": 326.24
            },
            {
              "end": 326.76,
              "word": "Yeah.",
              "start": 326.36
            },
            {
              "end": 326.76,
              "word": "So",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "that's",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "a",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "great",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "way",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "for",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "us",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "to",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "get",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "this",
              "start": 326.76
            },
            {
              "end": 326.76,
              "word": "done",
              "start": 326.76
            },
            {
              "end": 327.2,
              "word": "already.",
              "start": 326.76
            },
            {
              "end": 328.34,
              "word": "Um,",
              "start": 327.78
            },
            {
              "end": 328.88,
              "word": "so",
              "start": 328.52
            },
            {
              "end": 329.22,
              "word": "that",
              "start": 328.88
            },
            {
              "end": 329.58,
              "word": "together",
              "start": 329.22
            },
            {
              "end": 330,
              "word": "we",
              "start": 329.58
            },
            {
              "end": 330.18,
              "word": "can",
              "start": 330
            },
            {
              "end": 330.6,
              "word": "look",
              "start": 330.18
            },
            {
              "end": 330.9,
              "word": "at",
              "start": 330.6
            },
            {
              "end": 331.32,
              "word": "like",
              "start": 330.9
            },
            {
              "end": 331.68,
              "word": "what",
              "start": 331.32
            },
            {
              "end": 332,
              "word": "might",
              "start": 331.68
            },
            {
              "end": 332.18,
              "word": "be",
              "start": 332
            },
            {
              "end": 332.32,
              "word": "going",
              "start": 332.18
            },
            {
              "end": 332.76,
              "word": "on",
              "start": 332.32
            },
            {
              "end": 333.22,
              "word": "with",
              "start": 332.76
            },
            {
              "end": 333.52,
              "word": "her.",
              "start": 333.22
            },
            {
              "end": 334.68,
              "word": "Great.",
              "start": 334.12
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "371.56",
          "text": "Clear. That's good. That's great. Okay. And totally unrelated to that. Is it possible for me to just get a printout with the cholesterol just so I can reference those numbers? Uh, that'd be cool. Um, and then I will check with the front desk. Mm-hmm . I should be able to access some sort of version of those electronic health records. Don't you guys have like a portal that you can make available? Yeah. Okay. Cool. I brought it up with her in my appointment last week and she said that I would get a follow up email, but that didn't get sent, but I have a pretty generic name.",
          "start": "335.24",
          "words": [
            {
              "end": 335.8,
              "word": "Clear.",
              "start": 335.24
            },
            {
              "end": 336.12,
              "word": "That's",
              "start": 335.86
            },
            {
              "end": 336.28,
              "word": "good.",
              "start": 336.12
            },
            {
              "end": 336.7,
              "word": "That's",
              "start": 336.32
            },
            {
              "end": 336.98,
              "word": "great.",
              "start": 336.7
            },
            {
              "end": 337.46,
              "word": "Okay.",
              "start": 337.06
            },
            {
              "end": 338.02,
              "word": "And",
              "start": 337.54
            },
            {
              "end": 338.74,
              "word": "totally",
              "start": 338.02
            },
            {
              "end": 339.1,
              "word": "unrelated",
              "start": 338.74
            },
            {
              "end": 339.42,
              "word": "to",
              "start": 339.1
            },
            {
              "end": 339.56,
              "word": "that.",
              "start": 339.42
            },
            {
              "end": 339.74,
              "word": "Is",
              "start": 339.62
            },
            {
              "end": 339.84,
              "word": "it",
              "start": 339.74
            },
            {
              "end": 340.08,
              "word": "possible",
              "start": 339.84
            },
            {
              "end": 340.38,
              "word": "for",
              "start": 340.08
            },
            {
              "end": 340.5,
              "word": "me",
              "start": 340.38
            },
            {
              "end": 340.62,
              "word": "to",
              "start": 340.5
            },
            {
              "end": 340.8,
              "word": "just",
              "start": 340.62
            },
            {
              "end": 341,
              "word": "get",
              "start": 340.8
            },
            {
              "end": 341.14,
              "word": "a",
              "start": 341
            },
            {
              "end": 341.72,
              "word": "printout",
              "start": 341.14
            },
            {
              "end": 342.1,
              "word": "with",
              "start": 341.72
            },
            {
              "end": 342.24,
              "word": "the",
              "start": 342.1
            },
            {
              "end": 343.46,
              "word": "cholesterol",
              "start": 342.24
            },
            {
              "end": 344.44,
              "word": "just",
              "start": 343.46
            },
            {
              "end": 344.96,
              "word": "so",
              "start": 344.44
            },
            {
              "end": 345.1,
              "word": "I",
              "start": 344.96
            },
            {
              "end": 345.26,
              "word": "can",
              "start": 345.1
            },
            {
              "end": 345.96,
              "word": "reference",
              "start": 345.26
            },
            {
              "end": 346.24,
              "word": "those",
              "start": 345.96
            },
            {
              "end": 346.6,
              "word": "numbers?",
              "start": 346.24
            },
            {
              "end": 347.16,
              "word": "Uh,",
              "start": 346.74
            },
            {
              "end": 347.36,
              "word": "that'd",
              "start": 347.18
            },
            {
              "end": 347.48,
              "word": "be",
              "start": 347.36
            },
            {
              "end": 347.68,
              "word": "cool.",
              "start": 347.48
            },
            {
              "end": 349.72,
              "word": "Um,",
              "start": 349.16
            },
            {
              "end": 350.28,
              "word": "and",
              "start": 349.72
            },
            {
              "end": 350.46,
              "word": "then",
              "start": 350.28
            },
            {
              "end": 350.68,
              "word": "I",
              "start": 350.46
            },
            {
              "end": 350.88,
              "word": "will",
              "start": 350.68
            },
            {
              "end": 351.12,
              "word": "check",
              "start": 350.88
            },
            {
              "end": 351.32,
              "word": "with",
              "start": 351.12
            },
            {
              "end": 351.54,
              "word": "the",
              "start": 351.32
            },
            {
              "end": 351.9,
              "word": "front",
              "start": 351.54
            },
            {
              "end": 352.66,
              "word": "desk.",
              "start": 351.9
            },
            {
              "end": 353.46,
              "word": "Mm",
              "start": 353.06
            },
            {
              "end": 353.46,
              "word": "-hmm",
              "start": 353.46
            },
            {
              "end": 353.46,
              "word": ".",
              "start": 353.46
            },
            {
              "end": 353.5,
              "word": "I",
              "start": 353.46
            },
            {
              "end": 353.72,
              "word": "should",
              "start": 353.5
            },
            {
              "end": 353.96,
              "word": "be",
              "start": 353.72
            },
            {
              "end": 354.24,
              "word": "able",
              "start": 353.96
            },
            {
              "end": 354.48,
              "word": "to",
              "start": 354.24
            },
            {
              "end": 355,
              "word": "access",
              "start": 354.48
            },
            {
              "end": 355.64,
              "word": "some",
              "start": 355
            },
            {
              "end": 356.12,
              "word": "sort",
              "start": 355.64
            },
            {
              "end": 356.38,
              "word": "of",
              "start": 356.12
            },
            {
              "end": 356.82,
              "word": "version",
              "start": 356.38
            },
            {
              "end": 357.18,
              "word": "of",
              "start": 356.82
            },
            {
              "end": 357.68,
              "word": "those",
              "start": 357.18
            },
            {
              "end": 358.04,
              "word": "electronic",
              "start": 357.68
            },
            {
              "end": 358.38,
              "word": "health",
              "start": 358.04
            },
            {
              "end": 358.82,
              "word": "records.",
              "start": 358.38
            },
            {
              "end": 360.02,
              "word": "Don't",
              "start": 359.62
            },
            {
              "end": 360.1,
              "word": "you",
              "start": 360.02
            },
            {
              "end": 360.24,
              "word": "guys",
              "start": 360.1
            },
            {
              "end": 360.34,
              "word": "have",
              "start": 360.24
            },
            {
              "end": 360.46,
              "word": "like",
              "start": 360.34
            },
            {
              "end": 360.5,
              "word": "a",
              "start": 360.46
            },
            {
              "end": 360.88,
              "word": "portal",
              "start": 360.5
            },
            {
              "end": 361.1,
              "word": "that",
              "start": 360.88
            },
            {
              "end": 361.2,
              "word": "you",
              "start": 361.1
            },
            {
              "end": 361.38,
              "word": "can",
              "start": 361.2
            },
            {
              "end": 361.68,
              "word": "make",
              "start": 361.38
            },
            {
              "end": 362,
              "word": "available?",
              "start": 361.68
            },
            {
              "end": 362.44,
              "word": "Yeah.",
              "start": 362.26
            },
            {
              "end": 362.5,
              "word": "Okay.",
              "start": 362.44
            },
            {
              "end": 362.92,
              "word": "Cool.",
              "start": 362.6
            },
            {
              "end": 363.52,
              "word": "I",
              "start": 363.12
            },
            {
              "end": 363.7,
              "word": "brought",
              "start": 363.52
            },
            {
              "end": 363.84,
              "word": "it",
              "start": 363.7
            },
            {
              "end": 363.96,
              "word": "up",
              "start": 363.84
            },
            {
              "end": 364.08,
              "word": "with",
              "start": 363.96
            },
            {
              "end": 364.18,
              "word": "her",
              "start": 364.08
            },
            {
              "end": 364.28,
              "word": "in",
              "start": 364.18
            },
            {
              "end": 364.38,
              "word": "my",
              "start": 364.28
            },
            {
              "end": 364.66,
              "word": "appointment",
              "start": 364.38
            },
            {
              "end": 364.96,
              "word": "last",
              "start": 364.66
            },
            {
              "end": 365.46,
              "word": "week",
              "start": 364.96
            },
            {
              "end": 366.54,
              "word": "and",
              "start": 365.46
            },
            {
              "end": 366.86,
              "word": "she",
              "start": 366.54
            },
            {
              "end": 367.14,
              "word": "said",
              "start": 366.86
            },
            {
              "end": 367.28,
              "word": "that",
              "start": 367.14
            },
            {
              "end": 367.4,
              "word": "I",
              "start": 367.28
            },
            {
              "end": 367.5,
              "word": "would",
              "start": 367.4
            },
            {
              "end": 367.68,
              "word": "get",
              "start": 367.5
            },
            {
              "end": 367.8,
              "word": "a",
              "start": 367.68
            },
            {
              "end": 368.12,
              "word": "follow",
              "start": 367.8
            },
            {
              "end": 368.34,
              "word": "up",
              "start": 368.12
            },
            {
              "end": 368.66,
              "word": "email,",
              "start": 368.34
            },
            {
              "end": 368.92,
              "word": "but",
              "start": 368.8
            },
            {
              "end": 369.12,
              "word": "that",
              "start": 368.92
            },
            {
              "end": 369.32,
              "word": "didn't",
              "start": 369.12
            },
            {
              "end": 369.42,
              "word": "get",
              "start": 369.32
            },
            {
              "end": 369.74,
              "word": "sent,",
              "start": 369.42
            },
            {
              "end": 369.98,
              "word": "but",
              "start": 369.84
            },
            {
              "end": 370.12,
              "word": "I",
              "start": 369.98
            },
            {
              "end": 370.22,
              "word": "have",
              "start": 370.12
            },
            {
              "end": 370.32,
              "word": "a",
              "start": 370.22
            },
            {
              "end": 370.56,
              "word": "pretty",
              "start": 370.32
            },
            {
              "end": 371.14,
              "word": "generic",
              "start": 370.56
            },
            {
              "end": 371.56,
              "word": "name.",
              "start": 371.14
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "384.06",
          "text": "So I wonder if there could be a typo like in the email address or something like that. Yeah. So just check with Melissa. She'll be able to take care of that for you. Cool. Okay. With regards to the rib issue.",
          "start": "372.22",
          "words": [
            {
              "end": 372.62,
              "word": "So",
              "start": 372.22
            },
            {
              "end": 372.74,
              "word": "I",
              "start": 372.62
            },
            {
              "end": 373,
              "word": "wonder",
              "start": 372.74
            },
            {
              "end": 373.14,
              "word": "if",
              "start": 373
            },
            {
              "end": 373.28,
              "word": "there",
              "start": 373.14
            },
            {
              "end": 373.4,
              "word": "could",
              "start": 373.28
            },
            {
              "end": 373.58,
              "word": "be",
              "start": 373.4
            },
            {
              "end": 373.68,
              "word": "a",
              "start": 373.58
            },
            {
              "end": 374.1,
              "word": "typo",
              "start": 373.68
            },
            {
              "end": 374.34,
              "word": "like",
              "start": 374.1
            },
            {
              "end": 374.88,
              "word": "in",
              "start": 374.34
            },
            {
              "end": 375,
              "word": "the",
              "start": 374.88
            },
            {
              "end": 375.3,
              "word": "email",
              "start": 375
            },
            {
              "end": 375.6,
              "word": "address",
              "start": 375.3
            },
            {
              "end": 375.9,
              "word": "or",
              "start": 375.6
            },
            {
              "end": 376.1,
              "word": "something",
              "start": 375.9
            },
            {
              "end": 376.38,
              "word": "like",
              "start": 376.1
            },
            {
              "end": 376.56,
              "word": "that.",
              "start": 376.38
            },
            {
              "end": 376.74,
              "word": "Yeah.",
              "start": 376.6
            },
            {
              "end": 376.9,
              "word": "So",
              "start": 376.78
            },
            {
              "end": 377.02,
              "word": "just",
              "start": 376.9
            },
            {
              "end": 377.4,
              "word": "check",
              "start": 377.02
            },
            {
              "end": 377.56,
              "word": "with",
              "start": 377.4
            },
            {
              "end": 377.82,
              "word": "Melissa.",
              "start": 377.56
            },
            {
              "end": 378.44,
              "word": "She'll",
              "start": 378.04
            },
            {
              "end": 378.56,
              "word": "be",
              "start": 378.44
            },
            {
              "end": 378.74,
              "word": "able",
              "start": 378.56
            },
            {
              "end": 378.96,
              "word": "to",
              "start": 378.74
            },
            {
              "end": 379.16,
              "word": "take",
              "start": 378.96
            },
            {
              "end": 379.38,
              "word": "care",
              "start": 379.16
            },
            {
              "end": 379.4,
              "word": "of",
              "start": 379.38
            },
            {
              "end": 379.56,
              "word": "that",
              "start": 379.4
            },
            {
              "end": 379.88,
              "word": "for",
              "start": 379.56
            },
            {
              "end": 380.18,
              "word": "you.",
              "start": 379.88
            },
            {
              "end": 380.52,
              "word": "Cool.",
              "start": 380.3
            },
            {
              "end": 381.26,
              "word": "Okay.",
              "start": 380.86
            },
            {
              "end": 381.84,
              "word": "With",
              "start": 381.26
            },
            {
              "end": 382.24,
              "word": "regards",
              "start": 381.84
            },
            {
              "end": 382.6,
              "word": "to",
              "start": 382.24
            },
            {
              "end": 382.88,
              "word": "the",
              "start": 382.6
            },
            {
              "end": 383.62,
              "word": "rib",
              "start": 382.88
            },
            {
              "end": 384.06,
              "word": "issue.",
              "start": 383.62
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "385.46",
          "text": "Oh yeah. Yeah.",
          "start": "384.32",
          "words": [
            {
              "end": 384.56,
              "word": "Oh",
              "start": 384.32
            },
            {
              "end": 384.86,
              "word": "yeah.",
              "start": 384.56
            },
            {
              "end": 385.46,
              "word": "Yeah.",
              "start": 385.18
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "388.66",
          "text": "So is there any concern at all with that?",
          "start": "385.86",
          "words": [
            {
              "end": 386.38,
              "word": "So",
              "start": 385.86
            },
            {
              "end": 387,
              "word": "is",
              "start": 386.38
            },
            {
              "end": 387.18,
              "word": "there",
              "start": 387
            },
            {
              "end": 387.36,
              "word": "any",
              "start": 387.18
            },
            {
              "end": 387.78,
              "word": "concern",
              "start": 387.36
            },
            {
              "end": 388.02,
              "word": "at",
              "start": 387.78
            },
            {
              "end": 388.2,
              "word": "all",
              "start": 388.02
            },
            {
              "end": 388.44,
              "word": "with",
              "start": 388.2
            },
            {
              "end": 388.66,
              "word": "that?",
              "start": 388.44
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "402.01",
          "text": "Low concern. Low concern. Because I'm not feeling, you know, again, my mom, like, so I, yeah, I talked to my mom about most of these things. Yeah. She said the big indicator would be nausea.",
          "start": "389.26",
          "words": [
            {
              "end": 389.48,
              "word": "Low",
              "start": 389.26
            },
            {
              "end": 390.02,
              "word": "concern.",
              "start": 389.48
            },
            {
              "end": 390.6,
              "word": "Low",
              "start": 390.28
            },
            {
              "end": 390.6,
              "word": "concern.",
              "start": 390.6
            },
            {
              "end": 391,
              "word": "Because",
              "start": 390.68
            },
            {
              "end": 391.34,
              "word": "I'm",
              "start": 391
            },
            {
              "end": 391.54,
              "word": "not",
              "start": 391.34
            },
            {
              "end": 391.88,
              "word": "feeling,",
              "start": 391.54
            },
            {
              "end": 393.08,
              "word": "you",
              "start": 392.16
            },
            {
              "end": 394.87,
              "word": "know,",
              "start": 394.65
            },
            {
              "end": 395.65,
              "word": "again,",
              "start": 394.87
            },
            {
              "end": 395.85,
              "word": "my",
              "start": 395.73
            },
            {
              "end": 396.09,
              "word": "mom,",
              "start": 395.85
            },
            {
              "end": 396.41,
              "word": "like,",
              "start": 396.17
            },
            {
              "end": 396.85,
              "word": "so",
              "start": 396.45
            },
            {
              "end": 397.03,
              "word": "I,",
              "start": 396.85
            },
            {
              "end": 397.27,
              "word": "yeah,",
              "start": 397.11
            },
            {
              "end": 397.39,
              "word": "I",
              "start": 397.29
            },
            {
              "end": 397.69,
              "word": "talked",
              "start": 397.39
            },
            {
              "end": 397.79,
              "word": "to",
              "start": 397.69
            },
            {
              "end": 397.89,
              "word": "my",
              "start": 397.79
            },
            {
              "end": 398.09,
              "word": "mom",
              "start": 397.89
            },
            {
              "end": 398.31,
              "word": "about",
              "start": 398.09
            },
            {
              "end": 398.69,
              "word": "most",
              "start": 398.31
            },
            {
              "end": 398.85,
              "word": "of",
              "start": 398.69
            },
            {
              "end": 399.01,
              "word": "these",
              "start": 398.85
            },
            {
              "end": 399.35,
              "word": "things.",
              "start": 399.01
            },
            {
              "end": 399.61,
              "word": "Yeah.",
              "start": 399.43
            },
            {
              "end": 399.61,
              "word": "She",
              "start": 399.61
            },
            {
              "end": 400.11,
              "word": "said",
              "start": 399.61
            },
            {
              "end": 400.41,
              "word": "the",
              "start": 400.11
            },
            {
              "end": 400.59,
              "word": "big",
              "start": 400.41
            },
            {
              "end": 400.89,
              "word": "indicator",
              "start": 400.59
            },
            {
              "end": 401.23,
              "word": "would",
              "start": 400.89
            },
            {
              "end": 401.41,
              "word": "be",
              "start": 401.23
            },
            {
              "end": 402.01,
              "word": "nausea.",
              "start": 401.41
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "418.15",
          "text": "She, she was like, yeah, unless you were really like. Yeah. She, she was just like talking over the phone, but she's like, ah, it doesn't seem like a break to me.",
          "start": "404.15",
          "words": [
            {
              "end": 404.67,
              "word": "She,",
              "start": 404.15
            },
            {
              "end": 405.19,
              "word": "she",
              "start": 404.67
            },
            {
              "end": 407.33,
              "word": "was",
              "start": 405.19
            },
            {
              "end": 407.81,
              "word": "like,",
              "start": 407.33
            },
            {
              "end": 409.37,
              "word": "yeah,",
              "start": 407.95
            },
            {
              "end": 409.91,
              "word": "unless",
              "start": 409.51
            },
            {
              "end": 410.37,
              "word": "you",
              "start": 409.91
            },
            {
              "end": 410.49,
              "word": "were",
              "start": 410.37
            },
            {
              "end": 410.85,
              "word": "really",
              "start": 410.49
            },
            {
              "end": 411.31,
              "word": "like.",
              "start": 410.85
            },
            {
              "end": 411.69,
              "word": "Yeah.",
              "start": 411.39
            },
            {
              "end": 413.21,
              "word": "She,",
              "start": 412.81
            },
            {
              "end": 413.43,
              "word": "she",
              "start": 413.31
            },
            {
              "end": 413.61,
              "word": "was",
              "start": 413.43
            },
            {
              "end": 413.81,
              "word": "just",
              "start": 413.61
            },
            {
              "end": 413.99,
              "word": "like",
              "start": 413.81
            },
            {
              "end": 414.23,
              "word": "talking",
              "start": 413.99
            },
            {
              "end": 414.45,
              "word": "over",
              "start": 414.23
            },
            {
              "end": 414.61,
              "word": "the",
              "start": 414.45
            },
            {
              "end": 414.79,
              "word": "phone,",
              "start": 414.61
            },
            {
              "end": 414.93,
              "word": "but",
              "start": 414.87
            },
            {
              "end": 415.11,
              "word": "she's",
              "start": 414.93
            },
            {
              "end": 415.27,
              "word": "like,",
              "start": 415.11
            },
            {
              "end": 415.53,
              "word": "ah,",
              "start": 415.31
            },
            {
              "end": 415.81,
              "word": "it",
              "start": 415.65
            },
            {
              "end": 416.07,
              "word": "doesn't",
              "start": 415.81
            },
            {
              "end": 416.33,
              "word": "seem",
              "start": 416.07
            },
            {
              "end": 416.53,
              "word": "like",
              "start": 416.33
            },
            {
              "end": 416.65,
              "word": "a",
              "start": 416.53
            },
            {
              "end": 417.11,
              "word": "break",
              "start": 416.65
            },
            {
              "end": 417.93,
              "word": "to",
              "start": 417.11
            },
            {
              "end": 418.15,
              "word": "me.",
              "start": 417.93
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "418.89",
          "text": "Okay.",
          "start": "418.49",
          "words": [
            {
              "end": 418.89,
              "word": "Okay.",
              "start": 418.49
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "426.65",
          "text": "So she was like, yeah, you can definitely like impale yourself on an oar and have like a very uncomfortable two or three days.",
          "start": "419.75",
          "words": [
            {
              "end": 420.15,
              "word": "So",
              "start": 419.75
            },
            {
              "end": 420.55,
              "word": "she",
              "start": 420.15
            },
            {
              "end": 420.65,
              "word": "was",
              "start": 420.55
            },
            {
              "end": 420.75,
              "word": "like,",
              "start": 420.65
            },
            {
              "end": 420.95,
              "word": "yeah,",
              "start": 420.83
            },
            {
              "end": 421.07,
              "word": "you",
              "start": 420.97
            },
            {
              "end": 421.21,
              "word": "can",
              "start": 421.07
            },
            {
              "end": 421.51,
              "word": "definitely",
              "start": 421.21
            },
            {
              "end": 421.85,
              "word": "like",
              "start": 421.51
            },
            {
              "end": 422.33,
              "word": "impale",
              "start": 421.85
            },
            {
              "end": 422.63,
              "word": "yourself",
              "start": 422.33
            },
            {
              "end": 422.95,
              "word": "on",
              "start": 422.63
            },
            {
              "end": 423.05,
              "word": "an",
              "start": 422.95
            },
            {
              "end": 423.41,
              "word": "oar",
              "start": 423.05
            },
            {
              "end": 423.77,
              "word": "and",
              "start": 423.41
            },
            {
              "end": 424.01,
              "word": "have",
              "start": 423.77
            },
            {
              "end": 424.25,
              "word": "like",
              "start": 424.01
            },
            {
              "end": 424.37,
              "word": "a",
              "start": 424.25
            },
            {
              "end": 424.63,
              "word": "very",
              "start": 424.37
            },
            {
              "end": 425.19,
              "word": "uncomfortable",
              "start": 424.63
            },
            {
              "end": 425.95,
              "word": "two",
              "start": 425.19
            },
            {
              "end": 426.11,
              "word": "or",
              "start": 425.95
            },
            {
              "end": 426.29,
              "word": "three",
              "start": 426.11
            },
            {
              "end": 426.65,
              "word": "days.",
              "start": 426.29
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "427.77",
          "text": "Yeah.",
          "start": "427.37",
          "words": [
            {
              "end": 427.77,
              "word": "Yeah.",
              "start": 427.37
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "433.07",
          "text": "So, and I don't feel like, like in this moment right now, I have a discomfort of about a two.",
          "start": "428.13",
          "words": [
            {
              "end": 428.53,
              "word": "So,",
              "start": 428.13
            },
            {
              "end": 429.21,
              "word": "and",
              "start": 428.59
            },
            {
              "end": 429.39,
              "word": "I",
              "start": 429.21
            },
            {
              "end": 429.61,
              "word": "don't",
              "start": 429.39
            },
            {
              "end": 429.79,
              "word": "feel",
              "start": 429.61
            },
            {
              "end": 430.11,
              "word": "like,",
              "start": 429.79
            },
            {
              "end": 430.33,
              "word": "like",
              "start": 430.13
            },
            {
              "end": 430.53,
              "word": "in",
              "start": 430.33
            },
            {
              "end": 430.69,
              "word": "this",
              "start": 430.53
            },
            {
              "end": 431.01,
              "word": "moment",
              "start": 430.69
            },
            {
              "end": 431.21,
              "word": "right",
              "start": 431.01
            },
            {
              "end": 431.41,
              "word": "now,",
              "start": 431.21
            },
            {
              "end": 431.55,
              "word": "I",
              "start": 431.45
            },
            {
              "end": 431.69,
              "word": "have",
              "start": 431.55
            },
            {
              "end": 431.79,
              "word": "a",
              "start": 431.69
            },
            {
              "end": 432.15,
              "word": "discomfort",
              "start": 431.79
            },
            {
              "end": 432.43,
              "word": "of",
              "start": 432.15
            },
            {
              "end": 432.63,
              "word": "about",
              "start": 432.43
            },
            {
              "end": 432.77,
              "word": "a",
              "start": 432.63
            },
            {
              "end": 433.07,
              "word": "two.",
              "start": 432.77
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "434.69",
          "text": "Okay. Yeah.",
          "start": "433.73",
          "words": [
            {
              "end": 434.13,
              "word": "Okay.",
              "start": 433.73
            },
            {
              "end": 434.69,
              "word": "Yeah.",
              "start": 434.37
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "449.49",
          "text": "So do you, do you want any recommendations or anything? Because I think if you want us to go ahead, then we have to do like fiscal exams to just see what's going on. No.",
          "start": "437.33",
          "words": [
            {
              "end": 437.73,
              "word": "So",
              "start": 437.33
            },
            {
              "end": 438.03,
              "word": "do",
              "start": 437.73
            },
            {
              "end": 438.37,
              "word": "you,",
              "start": 438.03
            },
            {
              "end": 439.15,
              "word": "do",
              "start": 438.37
            },
            {
              "end": 439.37,
              "word": "you",
              "start": 439.15
            },
            {
              "end": 439.53,
              "word": "want",
              "start": 439.37
            },
            {
              "end": 439.69,
              "word": "any",
              "start": 439.53
            },
            {
              "end": 440.35,
              "word": "recommendations",
              "start": 439.69
            },
            {
              "end": 440.73,
              "word": "or",
              "start": 440.35
            },
            {
              "end": 440.99,
              "word": "anything?",
              "start": 440.73
            },
            {
              "end": 441.87,
              "word": "Because",
              "start": 441.43
            },
            {
              "end": 442.23,
              "word": "I",
              "start": 441.87
            },
            {
              "end": 442.51,
              "word": "think",
              "start": 442.23
            },
            {
              "end": 442.85,
              "word": "if",
              "start": 442.51
            },
            {
              "end": 443.01,
              "word": "you",
              "start": 442.85
            },
            {
              "end": 443.29,
              "word": "want",
              "start": 443.01
            },
            {
              "end": 443.45,
              "word": "us",
              "start": 443.29
            },
            {
              "end": 443.59,
              "word": "to",
              "start": 443.45
            },
            {
              "end": 443.73,
              "word": "go",
              "start": 443.59
            },
            {
              "end": 444.01,
              "word": "ahead,",
              "start": 443.73
            },
            {
              "end": 444.53,
              "word": "then",
              "start": 444.25
            },
            {
              "end": 444.75,
              "word": "we",
              "start": 444.53
            },
            {
              "end": 444.91,
              "word": "have",
              "start": 444.75
            },
            {
              "end": 445.07,
              "word": "to",
              "start": 444.91
            },
            {
              "end": 445.23,
              "word": "do",
              "start": 445.07
            },
            {
              "end": 445.39,
              "word": "like",
              "start": 445.23
            },
            {
              "end": 445.67,
              "word": "fiscal",
              "start": 445.39
            },
            {
              "end": 446.05,
              "word": "exams",
              "start": 445.67
            },
            {
              "end": 446.63,
              "word": "to",
              "start": 446.05
            },
            {
              "end": 447.93,
              "word": "just",
              "start": 446.63
            },
            {
              "end": 448.23,
              "word": "see",
              "start": 447.93
            },
            {
              "end": 448.67,
              "word": "what's",
              "start": 448.23
            },
            {
              "end": 448.85,
              "word": "going",
              "start": 448.67
            },
            {
              "end": 449.21,
              "word": "on.",
              "start": 448.85
            },
            {
              "end": 449.49,
              "word": "No.",
              "start": 449.35
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "474.71",
          "text": "No, I don't think, I don't think that's necessary. Okay. At this point. Okay. I think I just brought it up because you had asked in your questions, was there any changes since our last visit? And I felt like that would be dishonest for me to just casually leave out the fact that perhaps, but, um, no, I don't think there's any change. There's no need for any intervention or further. Okay.",
          "start": "449.49",
          "words": [
            {
              "end": 449.57,
              "word": "No,",
              "start": 449.49
            },
            {
              "end": 449.75,
              "word": "I",
              "start": 449.67
            },
            {
              "end": 449.97,
              "word": "don't",
              "start": 449.75
            },
            {
              "end": 450.17,
              "word": "think,",
              "start": 449.97
            },
            {
              "end": 450.33,
              "word": "I",
              "start": 450.17
            },
            {
              "end": 450.53,
              "word": "don't",
              "start": 450.33
            },
            {
              "end": 450.65,
              "word": "think",
              "start": 450.53
            },
            {
              "end": 450.91,
              "word": "that's",
              "start": 450.65
            },
            {
              "end": 451.43,
              "word": "necessary.",
              "start": 450.91
            },
            {
              "end": 452.11,
              "word": "Okay.",
              "start": 451.67
            },
            {
              "end": 452.37,
              "word": "At",
              "start": 452.15
            },
            {
              "end": 452.61,
              "word": "this",
              "start": 452.37
            },
            {
              "end": 452.99,
              "word": "point.",
              "start": 452.61
            },
            {
              "end": 453.59,
              "word": "Okay.",
              "start": 453.15
            },
            {
              "end": 453.67,
              "word": "I",
              "start": 453.63
            },
            {
              "end": 453.81,
              "word": "think",
              "start": 453.67
            },
            {
              "end": 454.57,
              "word": "I",
              "start": 453.81
            },
            {
              "end": 454.77,
              "word": "just",
              "start": 454.57
            },
            {
              "end": 455.01,
              "word": "brought",
              "start": 454.77
            },
            {
              "end": 455.23,
              "word": "it",
              "start": 455.01
            },
            {
              "end": 455.43,
              "word": "up",
              "start": 455.23
            },
            {
              "end": 455.77,
              "word": "because",
              "start": 455.43
            },
            {
              "end": 456.03,
              "word": "you",
              "start": 455.77
            },
            {
              "end": 456.17,
              "word": "had",
              "start": 456.03
            },
            {
              "end": 456.53,
              "word": "asked",
              "start": 456.17
            },
            {
              "end": 456.69,
              "word": "in",
              "start": 456.53
            },
            {
              "end": 456.77,
              "word": "your",
              "start": 456.69
            },
            {
              "end": 457.21,
              "word": "questions,",
              "start": 456.77
            },
            {
              "end": 457.43,
              "word": "was",
              "start": 457.29
            },
            {
              "end": 457.61,
              "word": "there",
              "start": 457.43
            },
            {
              "end": 457.81,
              "word": "any",
              "start": 457.61
            },
            {
              "end": 458.61,
              "word": "changes",
              "start": 457.81
            },
            {
              "end": 459.05,
              "word": "since",
              "start": 458.61
            },
            {
              "end": 459.19,
              "word": "our",
              "start": 459.05
            },
            {
              "end": 459.41,
              "word": "last",
              "start": 459.19
            },
            {
              "end": 459.77,
              "word": "visit?",
              "start": 459.41
            },
            {
              "end": 460.01,
              "word": "And",
              "start": 459.91
            },
            {
              "end": 460.13,
              "word": "I",
              "start": 460.01
            },
            {
              "end": 460.29,
              "word": "felt",
              "start": 460.13
            },
            {
              "end": 460.55,
              "word": "like",
              "start": 460.29
            },
            {
              "end": 461.13,
              "word": "that",
              "start": 460.55
            },
            {
              "end": 461.21,
              "word": "would",
              "start": 461.13
            },
            {
              "end": 461.37,
              "word": "be",
              "start": 461.21
            },
            {
              "end": 461.97,
              "word": "dishonest",
              "start": 461.37
            },
            {
              "end": 462.19,
              "word": "for",
              "start": 461.97
            },
            {
              "end": 462.33,
              "word": "me",
              "start": 462.19
            },
            {
              "end": 462.47,
              "word": "to",
              "start": 462.33
            },
            {
              "end": 462.67,
              "word": "just",
              "start": 462.47
            },
            {
              "end": 463.45,
              "word": "casually",
              "start": 462.67
            },
            {
              "end": 464.41,
              "word": "leave",
              "start": 463.45
            },
            {
              "end": 464.71,
              "word": "out",
              "start": 464.41
            },
            {
              "end": 465.03,
              "word": "the",
              "start": 464.71
            },
            {
              "end": 465.27,
              "word": "fact",
              "start": 465.03
            },
            {
              "end": 465.59,
              "word": "that",
              "start": 465.27
            },
            {
              "end": 466.05,
              "word": "perhaps,",
              "start": 465.59
            },
            {
              "end": 468.63,
              "word": "but,",
              "start": 466.39
            },
            {
              "end": 469.17,
              "word": "um,",
              "start": 468.77
            },
            {
              "end": 469.81,
              "word": "no,",
              "start": 469.17
            },
            {
              "end": 470.01,
              "word": "I",
              "start": 469.91
            },
            {
              "end": 470.23,
              "word": "don't",
              "start": 470.01
            },
            {
              "end": 470.39,
              "word": "think",
              "start": 470.23
            },
            {
              "end": 470.65,
              "word": "there's",
              "start": 470.39
            },
            {
              "end": 470.83,
              "word": "any",
              "start": 470.65
            },
            {
              "end": 470.97,
              "word": "change.",
              "start": 470.83
            },
            {
              "end": 471.15,
              "word": "There's",
              "start": 470.97
            },
            {
              "end": 471.15,
              "word": "no",
              "start": 471.15
            },
            {
              "end": 471.15,
              "word": "need",
              "start": 471.15
            },
            {
              "end": 471.25,
              "word": "for",
              "start": 471.15
            },
            {
              "end": 471.61,
              "word": "any",
              "start": 471.25
            },
            {
              "end": 472.87,
              "word": "intervention",
              "start": 471.61
            },
            {
              "end": 473.53,
              "word": "or",
              "start": 472.87
            },
            {
              "end": 473.91,
              "word": "further.",
              "start": 473.53
            },
            {
              "end": 474.71,
              "word": "Okay.",
              "start": 474.23
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "479.57",
          "text": "Good. Just making sure so that we do not just leave it hanging.",
          "start": "474.71",
          "words": [
            {
              "end": 475.03,
              "word": "Good.",
              "start": 474.71
            },
            {
              "end": 475.67,
              "word": "Just",
              "start": 475.17
            },
            {
              "end": 475.93,
              "word": "making",
              "start": 475.67
            },
            {
              "end": 476.27,
              "word": "sure",
              "start": 475.93
            },
            {
              "end": 476.53,
              "word": "so",
              "start": 476.27
            },
            {
              "end": 476.65,
              "word": "that",
              "start": 476.53
            },
            {
              "end": 476.95,
              "word": "we",
              "start": 476.65
            },
            {
              "end": 477.23,
              "word": "do",
              "start": 476.95
            },
            {
              "end": 477.67,
              "word": "not",
              "start": 477.23
            },
            {
              "end": 478.57,
              "word": "just",
              "start": 477.67
            },
            {
              "end": 479.07,
              "word": "leave",
              "start": 478.57
            },
            {
              "end": 479.23,
              "word": "it",
              "start": 479.07
            },
            {
              "end": 479.57,
              "word": "hanging.",
              "start": 479.23
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "484.61",
          "text": "Yes. I do not feel like it is just being left hanging.",
          "start": "480.45",
          "words": [
            {
              "end": 480.97,
              "word": "Yes.",
              "start": 480.45
            },
            {
              "end": 481.79,
              "word": "I",
              "start": 481.27
            },
            {
              "end": 481.95,
              "word": "do",
              "start": 481.79
            },
            {
              "end": 482.15,
              "word": "not",
              "start": 481.95
            },
            {
              "end": 482.49,
              "word": "feel",
              "start": 482.15
            },
            {
              "end": 482.81,
              "word": "like",
              "start": 482.49
            },
            {
              "end": 482.97,
              "word": "it",
              "start": 482.81
            },
            {
              "end": 483.09,
              "word": "is",
              "start": 482.97
            },
            {
              "end": 483.43,
              "word": "just",
              "start": 483.09
            },
            {
              "end": 483.81,
              "word": "being",
              "start": 483.43
            },
            {
              "end": 484.15,
              "word": "left",
              "start": 483.81
            },
            {
              "end": 484.61,
              "word": "hanging.",
              "start": 484.15
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "487.75",
          "text": "Okay.",
          "start": "487.23",
          "words": [
            {
              "end": 487.75,
              "word": "Okay.",
              "start": 487.23
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "489.77",
          "text": "Um, yeah. Okay.",
          "start": "487.77",
          "words": [
            {
              "end": 488.03,
              "word": "Um,",
              "start": 487.77
            },
            {
              "end": 489.03,
              "word": "yeah.",
              "start": 488.19
            },
            {
              "end": 489.77,
              "word": "Okay.",
              "start": 489.25
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "493.35",
          "text": "All right. Good. Good. Cool. All right. Any questions?",
          "start": "489.89",
          "words": [
            {
              "end": 490.25,
              "word": "All",
              "start": 489.89
            },
            {
              "end": 490.45,
              "word": "right.",
              "start": 490.25
            },
            {
              "end": 490.85,
              "word": "Good.",
              "start": 490.49
            },
            {
              "end": 491.75,
              "word": "Good.",
              "start": 491.23
            },
            {
              "end": 492.19,
              "word": "Cool.",
              "start": 491.85
            },
            {
              "end": 492.73,
              "word": "All",
              "start": 492.39
            },
            {
              "end": 492.87,
              "word": "right.",
              "start": 492.73
            },
            {
              "end": 493.03,
              "word": "Any",
              "start": 492.91
            },
            {
              "end": 493.35,
              "word": "questions?",
              "start": 493.03
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "496.03",
          "text": "I don't think so. I think I'm pretty clear. Okay.",
          "start": "493.87",
          "words": [
            {
              "end": 494.39,
              "word": "I",
              "start": 493.87
            },
            {
              "end": 494.51,
              "word": "don't",
              "start": 494.39
            },
            {
              "end": 494.61,
              "word": "think",
              "start": 494.51
            },
            {
              "end": 494.81,
              "word": "so.",
              "start": 494.61
            },
            {
              "end": 494.95,
              "word": "I",
              "start": 494.85
            },
            {
              "end": 495.03,
              "word": "think",
              "start": 494.95
            },
            {
              "end": 495.13,
              "word": "I'm",
              "start": 495.03
            },
            {
              "end": 495.31,
              "word": "pretty",
              "start": 495.13
            },
            {
              "end": 495.53,
              "word": "clear.",
              "start": 495.31
            },
            {
              "end": 496.03,
              "word": "Okay.",
              "start": 495.69
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "499.23",
          "text": "All right. So I'll just let them go ahead with the rest.",
          "start": "496.13",
          "words": [
            {
              "end": 496.53,
              "word": "All",
              "start": 496.13
            },
            {
              "end": 496.79,
              "word": "right.",
              "start": 496.53
            },
            {
              "end": 497.17,
              "word": "So",
              "start": 496.85
            },
            {
              "end": 497.55,
              "word": "I'll",
              "start": 497.17
            },
            {
              "end": 497.77,
              "word": "just",
              "start": 497.55
            },
            {
              "end": 497.99,
              "word": "let",
              "start": 497.77
            },
            {
              "end": 498.19,
              "word": "them",
              "start": 497.99
            },
            {
              "end": 498.31,
              "word": "go",
              "start": 498.19
            },
            {
              "end": 498.55,
              "word": "ahead",
              "start": 498.31
            },
            {
              "end": 498.89,
              "word": "with",
              "start": 498.55
            },
            {
              "end": 498.95,
              "word": "the",
              "start": 498.89
            },
            {
              "end": 499.23,
              "word": "rest.",
              "start": 498.95
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "500.07",
          "text": "All right.",
          "start": "499.23",
          "words": [
            {
              "end": 499.61,
              "word": "All",
              "start": 499.23
            },
            {
              "end": 500.07,
              "word": "right.",
              "start": 499.61
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "501.01",
          "text": "It was nice meeting you.",
          "start": "500.11",
          "words": [
            {
              "end": 500.25,
              "word": "It",
              "start": 500.11
            },
            {
              "end": 500.37,
              "word": "was",
              "start": 500.25
            },
            {
              "end": 500.53,
              "word": "nice",
              "start": 500.37
            },
            {
              "end": 500.81,
              "word": "meeting",
              "start": 500.53
            },
            {
              "end": 501.01,
              "word": "you.",
              "start": 500.81
            }
          ],
          "speaker": "SPEAKER_02"
        },
        {
          "end": "501.27",
          "text": "Thank you.",
          "start": "501.03",
          "words": [
            {
              "end": 501.19,
              "word": "Thank",
              "start": 501.03
            },
            {
              "end": 501.27,
              "word": "you.",
              "start": 501.19
            }
          ],
          "speaker": "SPEAKER_01"
        },
        {
          "end": "501.91",
          "text": "Nice to meet you.",
          "start": "501.35",
          "words": [
            {
              "end": 501.53,
              "word": "Nice",
              "start": 501.35
            },
            {
              "end": 501.67,
              "word": "to",
              "start": 501.53
            },
            {
              "end": 501.83,
              "word": "meet",
              "start": 501.67
            },
            {
              "end": 501.91,
              "word": "you.",
              "start": 501.83
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "508.99",
          "text": "You want me to schedule, schedule you now for the next one or do you want to wait?",
          "start": "502.79",
          "words": [
            {
              "end": 503.23,
              "word": "You",
              "start": 502.79
            },
            {
              "end": 503.37,
              "word": "want",
              "start": 503.23
            },
            {
              "end": 503.47,
              "word": "me",
              "start": 503.37
            },
            {
              "end": 503.59,
              "word": "to",
              "start": 503.47
            },
            {
              "end": 503.97,
              "word": "schedule,",
              "start": 503.59
            },
            {
              "end": 504.53,
              "word": "schedule",
              "start": 504.05
            },
            {
              "end": 504.95,
              "word": "you",
              "start": 504.53
            },
            {
              "end": 505.19,
              "word": "now",
              "start": 504.95
            },
            {
              "end": 505.53,
              "word": "for",
              "start": 505.19
            },
            {
              "end": 505.61,
              "word": "the",
              "start": 505.53
            },
            {
              "end": 506.95,
              "word": "next",
              "start": 505.61
            },
            {
              "end": 507.13,
              "word": "one",
              "start": 506.95
            },
            {
              "end": 508.27,
              "word": "or",
              "start": 507.13
            },
            {
              "end": 508.53,
              "word": "do",
              "start": 508.27
            },
            {
              "end": 508.63,
              "word": "you",
              "start": 508.53
            },
            {
              "end": 508.75,
              "word": "want",
              "start": 508.63
            },
            {
              "end": 508.79,
              "word": "to",
              "start": 508.75
            },
            {
              "end": 508.99,
              "word": "wait?",
              "start": 508.79
            }
          ],
          "speaker": "SPEAKER_01"
        },
        {
          "end": "579.45",
          "text": "Let's wait because, uh, yeah, because honestly what I, what I think is going to happen regardless is we will have a followup with that fertility plan. And what I think would be useful data is not just the labs, but also what, how this person reacted to it. Okay. Yeah. Because I, I, yeah, it just makes sense in that. And if I can collect all of that and present all of that, I think that gives you guys a better opportunity to kind of like be an advocate on my behalf. Sounds good. No, that's a good idea. Wait until you get your review from them. Yeah. And these fertility clinic can be quite busy. Uh, so I don't know if that's gonna, I will check with my partner just to see how that's been scheduled. Sounds good. But I'll, I'll go ahead. So we'll just not put anything on the calendar right now, but I'll check to get those, the access to the electronic. I think that's better than just printing it out because if I have access to those, I should be able to see the last labs.",
          "start": "511.35",
          "words": [
            {
              "end": 511.79,
              "word": "Let's",
              "start": 511.35
            },
            {
              "end": 512.11,
              "word": "wait",
              "start": 511.79
            },
            {
              "end": 512.97,
              "word": "because,",
              "start": 512.11
            },
            {
              "end": 514.19,
              "word": "uh,",
              "start": 513.33
            },
            {
              "end": 518.87,
              "word": "yeah,",
              "start": 518.53
            },
            {
              "end": 520.21,
              "word": "because",
              "start": 519.03
            },
            {
              "end": 520.61,
              "word": "honestly",
              "start": 520.21
            },
            {
              "end": 520.89,
              "word": "what",
              "start": 520.61
            },
            {
              "end": 521.07,
              "word": "I,",
              "start": 520.89
            },
            {
              "end": 521.37,
              "word": "what",
              "start": 521.09
            },
            {
              "end": 521.55,
              "word": "I",
              "start": 521.37
            },
            {
              "end": 521.71,
              "word": "think",
              "start": 521.55
            },
            {
              "end": 521.87,
              "word": "is",
              "start": 521.71
            },
            {
              "end": 522.09,
              "word": "going",
              "start": 521.87
            },
            {
              "end": 522.29,
              "word": "to",
              "start": 522.09
            },
            {
              "end": 522.57,
              "word": "happen",
              "start": 522.29
            },
            {
              "end": 523.17,
              "word": "regardless",
              "start": 522.57
            },
            {
              "end": 523.71,
              "word": "is",
              "start": 523.17
            },
            {
              "end": 523.91,
              "word": "we",
              "start": 523.71
            },
            {
              "end": 524.09,
              "word": "will",
              "start": 523.91
            },
            {
              "end": 524.25,
              "word": "have",
              "start": 524.09
            },
            {
              "end": 524.45,
              "word": "a",
              "start": 524.25
            },
            {
              "end": 524.97,
              "word": "followup",
              "start": 524.45
            },
            {
              "end": 525.15,
              "word": "with",
              "start": 524.97
            },
            {
              "end": 525.39,
              "word": "that",
              "start": 525.15
            },
            {
              "end": 526.37,
              "word": "fertility",
              "start": 525.39
            },
            {
              "end": 526.83,
              "word": "plan.",
              "start": 526.37
            },
            {
              "end": 527.93,
              "word": "And",
              "start": 527.49
            },
            {
              "end": 528.15,
              "word": "what",
              "start": 527.93
            },
            {
              "end": 528.29,
              "word": "I",
              "start": 528.15
            },
            {
              "end": 528.51,
              "word": "think",
              "start": 528.29
            },
            {
              "end": 528.65,
              "word": "would",
              "start": 528.51
            },
            {
              "end": 528.81,
              "word": "be",
              "start": 528.65
            },
            {
              "end": 529.19,
              "word": "useful",
              "start": 528.81
            },
            {
              "end": 529.59,
              "word": "data",
              "start": 529.19
            },
            {
              "end": 529.95,
              "word": "is",
              "start": 529.59
            },
            {
              "end": 530.15,
              "word": "not",
              "start": 529.95
            },
            {
              "end": 530.47,
              "word": "just",
              "start": 530.15
            },
            {
              "end": 530.61,
              "word": "the",
              "start": 530.47
            },
            {
              "end": 531.17,
              "word": "labs,",
              "start": 530.61
            },
            {
              "end": 531.49,
              "word": "but",
              "start": 531.21
            },
            {
              "end": 531.87,
              "word": "also",
              "start": 531.49
            },
            {
              "end": 532.17,
              "word": "what,",
              "start": 531.87
            },
            {
              "end": 532.51,
              "word": "how",
              "start": 532.19
            },
            {
              "end": 532.77,
              "word": "this",
              "start": 532.51
            },
            {
              "end": 533.11,
              "word": "person",
              "start": 532.77
            },
            {
              "end": 534.05,
              "word": "reacted",
              "start": 533.61
            },
            {
              "end": 534.41,
              "word": "to",
              "start": 534.05
            },
            {
              "end": 534.71,
              "word": "it.",
              "start": 534.41
            },
            {
              "end": 535.95,
              "word": "Okay.",
              "start": 535.51
            },
            {
              "end": 536.31,
              "word": "Yeah.",
              "start": 535.99
            },
            {
              "end": 536.65,
              "word": "Because",
              "start": 536.37
            },
            {
              "end": 536.81,
              "word": "I,",
              "start": 536.65
            },
            {
              "end": 537.03,
              "word": "I,",
              "start": 536.85
            },
            {
              "end": 537.57,
              "word": "yeah,",
              "start": 537.03
            },
            {
              "end": 537.81,
              "word": "it",
              "start": 537.71
            },
            {
              "end": 538.01,
              "word": "just",
              "start": 537.81
            },
            {
              "end": 538.21,
              "word": "makes",
              "start": 538.01
            },
            {
              "end": 538.57,
              "word": "sense",
              "start": 538.21
            },
            {
              "end": 538.73,
              "word": "in",
              "start": 538.57
            },
            {
              "end": 538.93,
              "word": "that.",
              "start": 538.73
            },
            {
              "end": 539.41,
              "word": "And",
              "start": 539.05
            },
            {
              "end": 539.55,
              "word": "if",
              "start": 539.41
            },
            {
              "end": 539.69,
              "word": "I",
              "start": 539.55
            },
            {
              "end": 539.93,
              "word": "can",
              "start": 539.69
            },
            {
              "end": 540.59,
              "word": "collect",
              "start": 539.93
            },
            {
              "end": 540.99,
              "word": "all",
              "start": 540.59
            },
            {
              "end": 541.13,
              "word": "of",
              "start": 540.99
            },
            {
              "end": 541.41,
              "word": "that",
              "start": 541.13
            },
            {
              "end": 541.55,
              "word": "and",
              "start": 541.41
            },
            {
              "end": 541.85,
              "word": "present",
              "start": 541.55
            },
            {
              "end": 542.11,
              "word": "all",
              "start": 541.85
            },
            {
              "end": 542.25,
              "word": "of",
              "start": 542.11
            },
            {
              "end": 542.59,
              "word": "that,",
              "start": 542.25
            },
            {
              "end": 543.77,
              "word": "I",
              "start": 542.63
            },
            {
              "end": 544.13,
              "word": "think",
              "start": 543.77
            },
            {
              "end": 544.25,
              "word": "that",
              "start": 544.13
            },
            {
              "end": 544.49,
              "word": "gives",
              "start": 544.25
            },
            {
              "end": 544.67,
              "word": "you",
              "start": 544.49
            },
            {
              "end": 544.85,
              "word": "guys",
              "start": 544.67
            },
            {
              "end": 544.97,
              "word": "a",
              "start": 544.85
            },
            {
              "end": 545.17,
              "word": "better",
              "start": 544.97
            },
            {
              "end": 545.69,
              "word": "opportunity",
              "start": 545.17
            },
            {
              "end": 546.03,
              "word": "to",
              "start": 545.69
            },
            {
              "end": 546.21,
              "word": "kind",
              "start": 546.03
            },
            {
              "end": 546.35,
              "word": "of",
              "start": 546.21
            },
            {
              "end": 546.61,
              "word": "like",
              "start": 546.35
            },
            {
              "end": 547.23,
              "word": "be",
              "start": 546.61
            },
            {
              "end": 547.59,
              "word": "an",
              "start": 547.23
            },
            {
              "end": 547.95,
              "word": "advocate",
              "start": 547.59
            },
            {
              "end": 548.19,
              "word": "on",
              "start": 547.95
            },
            {
              "end": 548.33,
              "word": "my",
              "start": 548.19
            },
            {
              "end": 548.59,
              "word": "behalf.",
              "start": 548.33
            },
            {
              "end": 548.99,
              "word": "Sounds",
              "start": 548.61
            },
            {
              "end": 549.03,
              "word": "good.",
              "start": 548.99
            },
            {
              "end": 549.77,
              "word": "No,",
              "start": 549.33
            },
            {
              "end": 549.93,
              "word": "that's",
              "start": 549.77
            },
            {
              "end": 549.99,
              "word": "a",
              "start": 549.93
            },
            {
              "end": 550.13,
              "word": "good",
              "start": 549.99
            },
            {
              "end": 550.37,
              "word": "idea.",
              "start": 550.13
            },
            {
              "end": 550.63,
              "word": "Wait",
              "start": 550.41
            },
            {
              "end": 550.93,
              "word": "until",
              "start": 550.63
            },
            {
              "end": 551.61,
              "word": "you",
              "start": 550.93
            },
            {
              "end": 551.83,
              "word": "get",
              "start": 551.61
            },
            {
              "end": 552.05,
              "word": "your",
              "start": 551.83
            },
            {
              "end": 552.37,
              "word": "review",
              "start": 552.05
            },
            {
              "end": 552.65,
              "word": "from",
              "start": 552.37
            },
            {
              "end": 552.91,
              "word": "them.",
              "start": 552.65
            },
            {
              "end": 553.61,
              "word": "Yeah.",
              "start": 553.17
            },
            {
              "end": 553.83,
              "word": "And",
              "start": 553.73
            },
            {
              "end": 553.95,
              "word": "these",
              "start": 553.83
            },
            {
              "end": 554.21,
              "word": "fertility",
              "start": 553.95
            },
            {
              "end": 554.67,
              "word": "clinic",
              "start": 554.21
            },
            {
              "end": 554.89,
              "word": "can",
              "start": 554.67
            },
            {
              "end": 555.03,
              "word": "be",
              "start": 554.89
            },
            {
              "end": 555.27,
              "word": "quite",
              "start": 555.03
            },
            {
              "end": 555.79,
              "word": "busy.",
              "start": 555.27
            },
            {
              "end": 557.39,
              "word": "Uh,",
              "start": 556.95
            },
            {
              "end": 557.83,
              "word": "so",
              "start": 557.39
            },
            {
              "end": 558.11,
              "word": "I",
              "start": 557.83
            },
            {
              "end": 558.37,
              "word": "don't",
              "start": 558.11
            },
            {
              "end": 558.63,
              "word": "know",
              "start": 558.37
            },
            {
              "end": 558.93,
              "word": "if",
              "start": 558.63
            },
            {
              "end": 559.21,
              "word": "that's",
              "start": 558.93
            },
            {
              "end": 559.49,
              "word": "gonna,",
              "start": 559.21
            },
            {
              "end": 560.41,
              "word": "I",
              "start": 559.61
            },
            {
              "end": 560.59,
              "word": "will",
              "start": 560.41
            },
            {
              "end": 560.75,
              "word": "check",
              "start": 560.59
            },
            {
              "end": 560.89,
              "word": "with",
              "start": 560.75
            },
            {
              "end": 561.03,
              "word": "my",
              "start": 560.89
            },
            {
              "end": 561.33,
              "word": "partner",
              "start": 561.03
            },
            {
              "end": 561.55,
              "word": "just",
              "start": 561.33
            },
            {
              "end": 561.67,
              "word": "to",
              "start": 561.55
            },
            {
              "end": 561.89,
              "word": "see",
              "start": 561.67
            },
            {
              "end": 562.01,
              "word": "how",
              "start": 561.89
            },
            {
              "end": 562.37,
              "word": "that's",
              "start": 562.01
            },
            {
              "end": 562.57,
              "word": "been",
              "start": 562.37
            },
            {
              "end": 563.19,
              "word": "scheduled.",
              "start": 562.57
            },
            {
              "end": 563.75,
              "word": "Sounds",
              "start": 563.45
            },
            {
              "end": 564.05,
              "word": "good.",
              "start": 563.75
            },
            {
              "end": 564.91,
              "word": "But",
              "start": 564.51
            },
            {
              "end": 565.11,
              "word": "I'll,",
              "start": 564.91
            },
            {
              "end": 565.47,
              "word": "I'll",
              "start": 565.11
            },
            {
              "end": 565.51,
              "word": "go",
              "start": 565.47
            },
            {
              "end": 565.71,
              "word": "ahead.",
              "start": 565.51
            },
            {
              "end": 565.87,
              "word": "So",
              "start": 565.77
            },
            {
              "end": 566.05,
              "word": "we'll",
              "start": 565.87
            },
            {
              "end": 566.25,
              "word": "just",
              "start": 566.05
            },
            {
              "end": 566.53,
              "word": "not",
              "start": 566.25
            },
            {
              "end": 566.77,
              "word": "put",
              "start": 566.53
            },
            {
              "end": 567.01,
              "word": "anything",
              "start": 566.77
            },
            {
              "end": 567.25,
              "word": "on",
              "start": 567.01
            },
            {
              "end": 567.31,
              "word": "the",
              "start": 567.25
            },
            {
              "end": 567.59,
              "word": "calendar",
              "start": 567.31
            },
            {
              "end": 567.79,
              "word": "right",
              "start": 567.59
            },
            {
              "end": 568.11,
              "word": "now,",
              "start": 567.79
            },
            {
              "end": 568.65,
              "word": "but",
              "start": 568.21
            },
            {
              "end": 568.83,
              "word": "I'll",
              "start": 568.65
            },
            {
              "end": 569.13,
              "word": "check",
              "start": 568.83
            },
            {
              "end": 569.35,
              "word": "to",
              "start": 569.13
            },
            {
              "end": 569.55,
              "word": "get",
              "start": 569.35
            },
            {
              "end": 569.91,
              "word": "those,",
              "start": 569.55
            },
            {
              "end": 570.21,
              "word": "the",
              "start": 569.95
            },
            {
              "end": 570.57,
              "word": "access",
              "start": 570.21
            },
            {
              "end": 570.81,
              "word": "to",
              "start": 570.57
            },
            {
              "end": 570.93,
              "word": "the",
              "start": 570.81
            },
            {
              "end": 571.25,
              "word": "electronic.",
              "start": 570.93
            },
            {
              "end": 573.05,
              "word": "I",
              "start": 572.65
            },
            {
              "end": 573.29,
              "word": "think",
              "start": 573.05
            },
            {
              "end": 573.67,
              "word": "that's",
              "start": 573.29
            },
            {
              "end": 573.81,
              "word": "better",
              "start": 573.67
            },
            {
              "end": 574.07,
              "word": "than",
              "start": 573.81
            },
            {
              "end": 574.23,
              "word": "just",
              "start": 574.07
            },
            {
              "end": 574.57,
              "word": "printing",
              "start": 574.23
            },
            {
              "end": 574.77,
              "word": "it",
              "start": 574.57
            },
            {
              "end": 574.95,
              "word": "out",
              "start": 574.77
            },
            {
              "end": 575.27,
              "word": "because",
              "start": 574.95
            },
            {
              "end": 576.51,
              "word": "if",
              "start": 575.27
            },
            {
              "end": 576.67,
              "word": "I",
              "start": 576.51
            },
            {
              "end": 576.79,
              "word": "have",
              "start": 576.67
            },
            {
              "end": 577.07,
              "word": "access",
              "start": 576.79
            },
            {
              "end": 577.29,
              "word": "to",
              "start": 577.07
            },
            {
              "end": 577.45,
              "word": "those,",
              "start": 577.29
            },
            {
              "end": 577.61,
              "word": "I",
              "start": 577.53
            },
            {
              "end": 577.75,
              "word": "should",
              "start": 577.61
            },
            {
              "end": 577.93,
              "word": "be",
              "start": 577.75
            },
            {
              "end": 578.01,
              "word": "able",
              "start": 577.93
            },
            {
              "end": 578.15,
              "word": "to",
              "start": 578.01
            },
            {
              "end": 578.43,
              "word": "see",
              "start": 578.15
            },
            {
              "end": 578.59,
              "word": "the",
              "start": 578.43
            },
            {
              "end": 579.01,
              "word": "last",
              "start": 578.59
            },
            {
              "end": 579.45,
              "word": "labs.",
              "start": 579.01
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "587.13",
          "text": "You don't want me to print it out? already printed it. Do you want it? I'll take it. Okay. Okay. Yeah. Perfect.",
          "start": "579.47",
          "words": [
            {
              "end": 579.77,
              "word": "You",
              "start": 579.47
            },
            {
              "end": 579.97,
              "word": "don't",
              "start": 579.77
            },
            {
              "end": 580.07,
              "word": "want",
              "start": 579.97
            },
            {
              "end": 580.21,
              "word": "me",
              "start": 580.07
            },
            {
              "end": 580.31,
              "word": "to",
              "start": 580.21
            },
            {
              "end": 580.49,
              "word": "print",
              "start": 580.31
            },
            {
              "end": 580.61,
              "word": "it",
              "start": 580.49
            },
            {
              "end": 580.77,
              "word": "out?",
              "start": 580.61
            },
            {
              "end": 582.55,
              "word": "already",
              "start": 582.15
            },
            {
              "end": 583.53,
              "word": "printed",
              "start": 582.55
            },
            {
              "end": 583.89,
              "word": "it.",
              "start": 583.53
            },
            {
              "end": 584.45,
              "word": "Do",
              "start": 584.05
            },
            {
              "end": 584.57,
              "word": "you",
              "start": 584.45
            },
            {
              "end": 584.77,
              "word": "want",
              "start": 584.57
            },
            {
              "end": 584.85,
              "word": "it?",
              "start": 584.77
            },
            {
              "end": 584.95,
              "word": "I'll",
              "start": 584.87
            },
            {
              "end": 585.13,
              "word": "take",
              "start": 584.95
            },
            {
              "end": 585.31,
              "word": "it.",
              "start": 585.13
            },
            {
              "end": 585.67,
              "word": "Okay.",
              "start": 585.39
            },
            {
              "end": 586.13,
              "word": "Okay.",
              "start": 585.73
            },
            {
              "end": 586.63,
              "word": "Yeah.",
              "start": 586.23
            },
            {
              "end": 587.13,
              "word": "Perfect.",
              "start": 586.73
            }
          ],
          "speaker": "SPEAKER_01"
        },
        {
          "end": "591.23",
          "text": "Thanks for being so transparent. Yeah. Thanks guys. Appreciate it. See ya.",
          "start": "587.29",
          "words": [
            {
              "end": 587.65,
              "word": "Thanks",
              "start": 587.29
            },
            {
              "end": 587.83,
              "word": "for",
              "start": 587.65
            },
            {
              "end": 588.03,
              "word": "being",
              "start": 587.83
            },
            {
              "end": 588.21,
              "word": "so",
              "start": 588.03
            },
            {
              "end": 588.77,
              "word": "transparent.",
              "start": 588.21
            },
            {
              "end": 589.31,
              "word": "Yeah.",
              "start": 589.09
            },
            {
              "end": 589.67,
              "word": "Thanks",
              "start": 589.31
            },
            {
              "end": 590.09,
              "word": "guys.",
              "start": 589.67
            },
            {
              "end": 590.71,
              "word": "Appreciate",
              "start": 590.17
            },
            {
              "end": 590.99,
              "word": "it.",
              "start": 590.71
            },
            {
              "end": 591.09,
              "word": "See",
              "start": 591.05
            },
            {
              "end": 591.23,
              "word": "ya.",
              "start": 591.09
            }
          ],
          "speaker": "SPEAKER_00"
        },
        {
          "end": "605.77",
          "text": "No, actually, to just check in with you about the",
          "start": "599.99",
          "words": [
            {
              "end": 600.55,
              "word": "No,",
              "start": 599.99
            },
            {
              "end": 601.07,
              "word": "actually,",
              "start": 600.75
            },
            {
              "end": 603.47,
              "word": "to",
              "start": 603.01
            },
            {
              "end": 604.01,
              "word": "just",
              "start": 603.47
            },
            {
              "end": 604.99,
              "word": "check",
              "start": 604.01
            },
            {
              "end": 605.15,
              "word": "in",
              "start": 604.99
            },
            {
              "end": 605.29,
              "word": "with",
              "start": 605.15
            },
            {
              "end": 605.45,
              "word": "you",
              "start": 605.29
            },
            {
              "end": 605.63,
              "word": "about",
              "start": 605.45
            },
            {
              "end": 605.77,
              "word": "the",
              "start": 605.63
            }
          ],
          "speaker": "SPEAKER_00"
        }
      ]

mp3transcript_clean = process_transcript(mp3transcript)

print("mp3 transcipt", mp3transcript_clean)
