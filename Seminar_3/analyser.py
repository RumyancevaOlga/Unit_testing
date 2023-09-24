class MoodAnalyser:

    def mood_analyser(self, msg: str) -> str:
        words = ('веселое', 'счастливое', 'грустное')
        for word in words:
            if word in msg:
                return word
        return 'неизвестное'
