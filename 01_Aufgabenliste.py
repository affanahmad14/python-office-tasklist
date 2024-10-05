# Aufgabenliste für Büroprojekte

aufgabenliste = []      # Definition einer Liste

def taskmanager():             # Definieren einer Funktion namens taskmanager
        task = input("Welche neue Aufgabe ist geplant? ")     #Abfrage nach der Aufgabe.
        aufgabenliste.append(task)  #Hinzufügen der Aufgabe zur Liste   
        print(f"Die Aufgabe '{task}' wurde der Todo Liste hinzugefügt") 

def show_aufgabenliste():
        if aufgabenliste: 
                print("Deine Aufgabenliste:")
                for task in aufgabenliste:
                    print(task)
                        
        else: 
                print("Die Aufgabenliste ist leer")

def main():
        while True:
                print("\n ---Aufgabenliste---")
                print("1. Aufgabe hinzufügen")
                print("2. Aufgabenliste anzeigen")
                print("3. Programm beenden")
                choice = input("Bitte treffen sie ihre Auswahl: \n")

                if choice == "1":
                        print("Sie haben die 1 gewählt")
                        taskmanager()
                elif choice == "2":
                        print("Sie haben die 2 gewählt")
                        show_aufgabenliste()
                elif choice == "3":
                        print("Good Bye")
                        break
                else:
                        print("Bitte wählen sie zwischen 1, 2 oder drei")

main()



































              


