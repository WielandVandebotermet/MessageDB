from kivy.lang import Builder
from kivymd.app import MDApp
import pymongo


conn_str = "mongodb+srv://Wieland:<Password>.@cluster0.m6twp.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.ProffesionalSkills

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file('db.kv')

    def submit(self):
        values = (self.root.ids.word_input.text)
        if(len(values) > 0):
            ProffesionalSkills = {
                "message": values
            }
            db.Message.insert_one(ProffesionalSkills)
            self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'
            self.root.ids.word_input.text = ""
        else:
            self.root.ids.word_label.text = f'Nothing Added no text input'
            self.root.ids.word_input.text = ""

    def show(self):
        word = ""

        for post in db.Message.find({}, {"message": 1, "_id": False}):
            a = str(post)[13:]
            a = a[0:len(a) - 2]
            word = " " + a + "\n" + "\n" + word
            self.root.ids.word_label.text = word

MainApp().run()