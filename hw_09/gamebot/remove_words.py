def remove_words_with_substr(orig_str: str, substr: str = "абв") -> str:
    '''Удаляет из строки "orig_str" слова содержащие подстроку "substr"'''
    result_words = []
    for word in orig_str.split():
        if word.lower().find(substr) == -1:
            result_words.append(word)
    return ' '.join(result_words)


def remove_words(message, bot):
    '''Удаляет слова содержащие "абв"'''
    result = remove_words_with_substr(message.text)
    bot.send_message(message.chat.id, result)