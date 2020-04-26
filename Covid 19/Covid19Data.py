import tkinter as tk

from PIL import ImageTk, Image
import requests
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_data(country):
    url = "https://api.covid19api.com/"

    try:
        if country.lower() == 'global':
            url = url + 'summary'
            response = requests.request("GET", url)
            data = response.json()
            ans = ''
            for i in data['Global']:
                ans = ans + "\n" + i + ": " + str(data['Global'][i])
            label['text'] = ans
            print('The New cases confirmed and the new deaths and recoveries shown are the stats for today.')

        elif (country.lower() == 'usa') or (country.lower() == 'us') or (
                country.lower() == 'united states of america') or (
                country.lower() == 'the united states of america'):
            url = "https://corona.lmao.ninja/v2/countries/USA"

            payload = {}
            headers = {
                'Cookie': '__cfduid=d200d71060eb7fc135ca56ddd5f37e7041586929559'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()
            label['text'] = "Total Cases: " + str(data['cases']) + "\n" + "Deaths: " + str(data['deaths']) + "\n" + "Recovered: " + str(data['recovered'])
        else:
            if (country.lower() == 'uk') or (country.lower() == 'england') or (country.lower() == 'great britain'):
                country = 'United Kingdom'
            if country.lower() == 'uae':
                country = 'United Arab Emirates'
            country = country.replace(' ', '-').lower()
            url = url + 'summary'
            response = requests.request("GET", url)
            data = response.json()
            final = ''
            for i in data['Countries']:
                if i['Country'].lower() == country:
                    for j in i:
                        if (j != 'CountryCode') & (j != 'Slug') & (j != 'Date'):
                            final = final + '\n' + j + ': ' + str(i[j])
            label['text'] = final
            exit
    except:
        label['text'] = "The data hasn't been updated yet."


app = tk.Tk()  # command for making dialog box.

canvas = tk.Canvas(app, height = 500, width = 600)
canvas.pack()

image = Image.open('coronavirus.jpg')
image = image.resize((600, 500))
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(app, bg='#000000', bd=5)  # Makes a frame in app.
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') # Places the frame and changes its size and location.

# You can also use grid function with following syntax : .grid(row= value, column= value)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.68, relheight=1, )

button = tk.Button(frame, text="Get Data", command=lambda: get_data(entry.get())) # Code for adding a button.
button.place(relx=0.7, relheight=1, relwidth=0.3) # Places the button in the dialog box.

lower_frame = tk.Frame(app, bg='#000000', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

label = tk.Label(lower_frame, font=40, anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

app.mainloop()