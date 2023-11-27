import user_time
import location
import weather
import app_handler
import eng_dictionary
import play_music
import internet_search

import webbrowser

user_info = {'bot_name': "Groot"}


def event_handling(inp, tag, reply):
    if tag == 'CurrentHumanNameQuery':
        for val in internet_search.search_google(inp):
            print(val)
    # print(internet_search.search_google(inp))
    if tag == "GreetingResponse":
        user_info['name'] = inp.split()[-1]

    if tag == "CurrentHumanAgeQueryResponse":
        inp = inp.split()
        for curr in inp:
            if curr.isnumeric():
                user_info['age'] = curr

    if tag == "AppOpeningQuery":
        app_name = ' '.join(inp.split()[1:])
        if app_name in app_handler.installed_apps:
            if app_name in app_handler.opened_apps:
                return f'{app_name} is already opened'
            app_handler.open_application(app_name)
            app_handler.opened_apps.append(app_name)
            return reply.replace("<APPLICATION>", app_name)
        return f'{app_name} not found'

    if tag == "AppClosingQuery":
        app_name = inp.split()[-1]
        if app_name in app_handler.opened_apps:
            app_handler.opened_apps.remove(app_name)
            app_handler.close_application(app_name)
            return reply.replace("<APPLICATION>", app_name)
        return f'{app_name} is already closed'

    if tag == "TimeQuery":
        return reply.replace("<TIME>", user_time.get_time())

    if tag == "WeatherQuery":
        user_city = location.get_city()
        user_weather = weather.get_weather(user_city)

        if "temperature" not in reply:
            return reply.replace("<WEATHER>", 'Cloudy')
        return reply.replace("<WEATHER>", 'Cloudy')

    if tag == "MeaningQuery":
        query_word = inp.split()[-1]
        dict_data = eng_dictionary.get_dictionary_entry(query_word)
        return dict_data[0]['meanings'][0]['definitions'][0]['definition']

    if tag == "SongQuery":
        song_name = ' '.join(inp.split()[1:])
        song_id = play_music.get_youtube_video_id(song_name)
        video_url = play_music.video_url.replace("<ID>", song_id)
        webbrowser.open(video_url)
        return reply.replace("<SONG_NAME>", song_name)

    if "<HUMAN>" in reply:
        if 'name' in user_info:
            return reply.replace("<HUMAN>", user_info['name'])
        return "I don't know your name."

    if "<AGE>" in reply:
        if 'age' in user_info:
            return reply.replace("<AGE>", user_info['age'])
        return "I don't know your age"

    if "<BOT_NAME>" in reply:
        return reply.replace("<BOT_NAME>", user_info['bot_name'])

    return reply
