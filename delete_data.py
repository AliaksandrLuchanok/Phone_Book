def delete_data(use_list):
  count = int(use_list[:16])
  # print (count)
  with open('phone_book.txt','r', encoding = 'utf-8') as data:
    text_string = data.readlines()    
  with open('phone_book.txt','w', encoding = 'utf-8') as data_w:
    data_w.writelines(text_string[:count])
    second_text = None
    if count+1 < len (text_string):
      second_text = [str(int(el[:16])-1)+ ' '*(16-len(str(int(el[:16])-1)))+el[16:] for el in text_string[count+1:]]
      data_w.writelines(second_text)
 
