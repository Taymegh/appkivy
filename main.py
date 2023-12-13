from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        self.theme = None 
        layout = BoxLayout(orientation='vertical')
        # Boutons pour sélectionner le thème
        theme_buttons = BoxLayout(orientation='horizontal')
        theme_buttons.add_widget(Button(text='Thème 1', on_press=self.select_theme))
        theme_buttons.add_widget(Button(text='Thème 2', on_press=self.select_theme))
        theme_buttons.add_widget(Button(text='Thème 3', on_press=self.select_theme))
        layout.add_widget(theme_buttons)

        # Conteneur pour les questions
        self.question_container = BoxLayout(orientation='vertical')
        layout.add_widget(self.question_container)

        return layout

    def select_theme(self, instance):
        # Réinitialiser le conteneur de questions
        self.question_container.clear_widgets()

        # Mettre à jour le thème sélectionné
        self.theme = instance.text

        # Charger les questions en fonction du thème
        questions = self.load_questions_for_theme()

        # Ajouter les questions à l'interface utilisateur
        for q in questions:
            question_label = Label(text=q["question"])
            self.question_container.add_widget(question_label)

            for option in q["options"]:
                btn = Button(text=option, on_press=self.check_answer)
                self.question_container.add_widget(btn)

    def load_questions_for_theme(self):
        # Charger les questions en fonction du thème sélectionné
        # Vous pouvez implémenter cette fonction pour lire les questions depuis un fichier, une base de données, etc.
        if self.theme == 'Thème 1':
            return [
                {"question": "Quelle est la capitale de la France?", "options": ["Paris", "Londres", "Berlin"], "correct": "Paris"},
                # Ajoutez d'autres questions pour Thème 1
            ]
        elif self.theme == 'Thème 2':
            return [
                {"question": "Quelle est la planète la plus proche du soleil?", "options": ["Vénus", "Terre", "Mercure"], "correct": "Mercure"},
                # Ajoutez d'autres questions pour Thème 2
            ]
        elif self.theme == 'Thème 3':
            return [
                {"question": "Quel langage de programmation utilise le framework Kivy?", "options": ["Python", "Java", "C++"], "correct": "Python"},
                # Ajoutez d'autres questions pour Thème 3
            ]
        else:
            return []  # Thème non reconnu

    def check_answer(self, instance):
        selected_option = instance.text
        # Logique de vérification de la réponse ici
        pass

if __name__ == '__main__':
    QuizApp().run()
