"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
"""
from insert_data import *
from delete_data import *
#↓↓↓ РЕДАКТИРОВАНИЕ ДАННЫХ БЛОКНОТА:
def edit_data(use_string):
  use_string = use_string.split()
  new_data = list()
  new_data.append(use_string[0]+' '*(16-len(use_string[0])))
  print(*use_string)
  for el in use_string[1:]:
    print(f'Текущее значение - {el}:')
    use_choise = input('оставить без изменений - введите 0'  + '\n' +
                     'редактировать          - введите новое значение: ').replace(' ','').upper()
    if use_choise != '0':  new_data.append(use_choise + ' '*(16-len(use_choise)))
    else: new_data.append(el + ' '*(16-len(el)))
  print (*new_data)
  use_choise = input('подтвердить внесение изменений - введите 1' + '\n' +
                     'редактировать изменения        - введите 2' + '\n' +
                     'вернуться в главное меню       - введите 3' + '\n' +
                     'завершить работу               - введите 4' + '\n').replace(' ','')
  
  if (use_choise)   == "1": 
    insert_data(new_data)
    get_data()
    start_programm()
  elif(use_choise)  == "2": 
    edit_data(''.join(new_data))
  elif(use_choise)  == "3": start_programm() 
  elif(use_choise)  == "4": return
  else: 
      print("Ошибка выбора!")
      edit_data(''.join(new_data))
#↑↑↑ РЕДАКТИРОВАНИЕ ДАННЫХ БЛОКНОТА:


#↓↓↓ 2 ПОИСК В ЛИСТЕ ПО ДОПОЛНИТЕЛЬНЫМ ПАРАМЕТРАМ:
def search_list (use_list):
  list_moovie = ["позицию: ","фамилию: ","имя: ","отчество: ","номер телефона в формате +37529-111-11-11: "]
  use_choise = input("Выберете дополнительную позицию поиска по: " + "\n"
        "позиции                  - введите 1" + "\n" +          
        "фамилии                  - введите 2" + "\n" +
        "имени                    - введите 3" + "\n" +
        "отчеству                 - введите 4" + "\n" +
        "номеру телефона          - введите 5" + "\n" +
        "вернуться в главное меню - введите 6" + "\n" +
        "завершить работу         - введите 7" + "\n" +
        ": ").replace(" ","")
  temp_list = list()
  if  (use_choise)  in ["1","2","3","4","5"]: 
    use_data = input(f"Введите {list_moovie[int(use_choise)-1]}").replace(' ','').upper()
    temp_list.append(use_list[0])
    for el in use_list:
      if use_data in list(el.split())[int(use_choise)-1]:
        print(list(el.split())[int(use_choise)-1])
        temp_list.append(el)
    if len(temp_list) < 2:
      print("По заданным параметрам результатов нет! ")
      start_programm()
    else:
      if len (temp_list) == 2:
        print (*temp_list)
        use_choise = input('Выберете действие:' + "\n" +
              'удалить абонента          - введите 1' + "\n" +             
              'редактировать данные      - введите 2' + "\n" + 
              'вернуться в главное меню  - введите 3' + "\n" + 
              'завершить работу          - введите 4' + "\n").replace(' ','')
        if    (use_choise)  == '1': 
          delete_data(temp_list[1])
          get_all_data()
          start_programm()        
        elif  (use_choise)  == '2': edit_data(temp_list[1])
        elif  (use_choise)  == '3': start_programm() 
        elif  (use_choise)  == "4": return        
        else: 
          print("Oшибка выбора!")
          search_list (temp_list)
      else:
        print (*temp_list)
        use_choise = input('Если необходимо:' + "\n" +
              'ввести дополнительные параметры поиска - введите 1' + "\n" + 
              'вернуться в главное меню               - введите 2' + "\n" + 
              'завершить работу                       - введите 3' + "\n").replace(' ','')
        if    (use_choise)  == '1': search_list (temp_list)
        elif  (use_choise)  == '2': start_programm() 
        elif  (use_choise)  == "3": return        
        else: 
          print("Oшибка выбора!")
          search_list (temp_list)
  elif(use_choise)  == "6": start_programm() 
  elif(use_choise)  == "7": return        
  else: 
      print("Oшибка выбора!")
      search_list(use_list)
#↑↑↑ 2 ПОИСК В ЛИСТЕ ПО ДОПОЛНИТЕЛЬНЫМ ПАРАМЕТРАМ: 


#↓↓↓ 1 ПОИСК ПО АРГУМЕНТУ С ЗАПИСЬЮ ИСКОМОГО В СПИСОК
def search_argument(index, argument):
   use_list = list()
   with open('phone_book.txt','r',encoding='utf-8') as data:
      line = data.readline()
      line_searh = list(line.split())
      use_list.append(' ' + line)
      while line:
        if argument in line_searh[index]: 
          use_list.append(line)
        line = data.readline()
        line_searh = list(line.split())
      if len(use_list) < 2:
         print("По заданным параметрам результатов нет! ")
         start_programm()
      else:
        if len (use_list) == 2:
          print (*use_list)
          use_choise = input('Выберете действие:' + "\n" +
                'удалить абонента          - введите 1' + "\n" +
                'редактировать данные      - введите 2' + "\n" + 
                'вернуться в главное меню  - введите 3' + "\n" + 
                'завершить работу          - введите 4' + "\n").replace(' ','')
          if    (use_choise)  == '1': 
            delete_data(use_list[1])
            get_all_data()
            start_programm()
          elif  (use_choise)  == '2': edit_data(use_list[1])
          elif  (use_choise)  == '3': start_programm() 
          elif  (use_choise)  == '4': return        
          else: 
            print("Oшибка выбора!")
            search_argument(index, argument)
        else:
          print (*use_list)
          use_choise = input('Если необходимо:' + "\n" +
                'ввести дополнительные параметры поиска - введите 1' + "\n" + 
                'вернуться в главное меню               - введите 2' + "\n" + 
                'завершить работу                       - введите 3' + "\n").replace(' ','')
          if    (use_choise)  == '1': search_list (use_list)
          elif  (use_choise)  == '2': start_programm() 
          elif  (use_choise)  == "3": return        
          else: 
            print("Oшибка выбора!")
            search_argument(index, argument)
#↑↑↑ 1 ПОИСК ПО АРГУМЕНТУ С ЗАПИСЬЮ ИСКОМОГО В СПИСОК        


#↓↓↓ 0 НАЧАЛО ПОИСКА 
def search_data ():
  list_moovie = ["позицию: ","фамилию: ","имя: ","отчество: ","номер телефона в формате +37529-111-11-11: "]
  use_choise = input("Параметр поиска по: " + "\n"
        "позиции                  - введите 1" + "\n" +          
        "фамилии                  - введите 2" + "\n" +
        "имени                    - введите 3" + "\n" +
        "отчеству                 - введите 4" + "\n" +
        "номеру телефона          - введите 5" + "\n" +
        "вернуться в главное меню - введите 6" + "\n" +
        "завершить работу         - введите 7" + "\n" +
        ": ").replace(" ","")
  if  (use_choise)  in ["1","2","3","4","5"]: 
    use_data = input(f"Введите {list_moovie[int(use_choise)-1]}").replace(' ','').upper()
    search_argument(int(use_choise)-1, use_data)
  elif(use_choise)  == "6": start_programm() 
  elif(use_choise)  == "7": return()         
  else: 
      print("Oшибка выбора!")
      search_data()
#↑↑↑ 0 НАЧАЛО ПОИСКА 

list_heading = ["ПОЗИЦИЯ", "ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", "НОМЕР ТЕЛЕФОНА"]
# ЗАПИСЬ СТРОКИ С АТРИБУТАМИ
# with open("phone_book.txt", "a", encoding = "utf-8") as data: 
#   for i in list_heading:
#     data.write(i + " "*(16-len(i)))
#   data.write("\n")

#↓↓↓ФУНКЦИЯ ИНФОРМАЦИОННОГО ТАБЛО С ДЕЙСТВИЯМИ
def get_data():
  use_choise = input("Выберете действие, которой хотите совершить: " + "\n"
        "вывести все данные       - введите 1" + "\n" +
        "задать параметры поиска  - введите 2" + "\n" +
        "вернуться в главное меню - введите 3" + "\n" +
        "завершить работу         - введите 4" + "\n" +
        ": ").replace(" ","")
  if  (use_choise)  == "1": get_all_data()    # +
  elif(use_choise)  == "2": search_data()     # +
  elif(use_choise)  == "3": start_programm()  # +
  elif(use_choise)  == "4": return()          # +
  else: 
      print("Ошибка выбора!")
      get_data()
#↑↑↑ФУНКЦИЯ ИНФОРМАЦИОННОГО ТАБЛО С ДЕЙСТВИЯМИ

#↓↓↓ВЫВОД ВСЕХ ДАННЫХ 
def get_all_data():
   with open("phone_book.txt","r", encoding = "utf-8") as data:
    line = data.readlines()
    for el in line:
      print(el[:-1])
    flag = input('Если желаете:' + '\n' +
          'продолжить          - введите 1' + '\n' +
          'завершить программу - введите любой символ'+ '\n')
    if flag != '1':
      return()
    start_programm()
#↑↑↑ВЫВОД ВСЕХ ДАННЫХ     
    
#↓↓↓ВВОД НОВОГО АБОНЕНТА 
def data_input(list_heading):
  with open("phone_book.txt", "r", encoding = "utf-8") as data:
    count = 0
    list_use = list()
    list_use.append(str(count))
    list_use.append(input("Введите фамилию: ").replace(" ","").upper())
    list_use.append(input("Введите имя: ").replace(" ","").upper())
    list_use.append(input("Введите отчество: ").replace(" ","").upper())
    list_use.append(input("Введите номер телефона в формате +37529-111-11-11: ").replace(" ",""))
    insert_data([el + " "*(15-len(el)) for el in list_use])
    get_all_data()
    start_programm()
#↑↑↑ВВОД НОВОГО АБОНЕНТА      


#СТАРТ ПРОГРАММЫ
def start_programm():
    use_choise = input("ГЛАВНОЕ МЕНЮ. Выберете действие, которой хотите совершить: " + "\n"
          "найти данные           - введите 1" + "\n" +
          "внести нового абонента - введите 2" + "\n" +
          "завершить работу       - введите 3" + "\n" +
          ": ").replace(" ","")
    if (use_choise)   == "1": get_data()
    elif(use_choise)  == "2": data_input(list_heading)
    elif(use_choise)  == "3": return
    else: 
       print("Ошибка выбора!")
       start_programm()
#СТАРТ ПРОГРАММЫ

start_programm()

