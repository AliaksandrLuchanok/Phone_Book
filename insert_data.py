
def insert_data(use_list):
  exam_string = ' '.join(use_list[1:])
  count = 1
  with open('phone_book.txt','r', encoding = 'utf-8') as data:
    text_string = data.readlines()
    for el in text_string[1:]:
      if exam_string > el[16:]:
        count +=1
  new_data = str(count)+' '*(16-len(str(count))) + str(exam_string)

  with open('phone_book.txt','w', encoding = 'utf-8') as data_w:
    data_w.writelines(text_string[:count])
    data_w.write(new_data + '\n')
    second_text = None
    if count+1 < len (text_string):
      second_text = [str(int(el[:16])+1)+ ' '*(16-len(str(int(el[:16])+1)))+el[16:] for el in text_string[count:]]
      data_w.writelines(second_text)


use_string = ['3              ', 'ЮЮЭЕНОК        ', 'АЛЕКСАНДР      ', 'АЛЕКСАНДРОВИЧ  ', '+37529-654-89-24']

insert_data(use_string)
