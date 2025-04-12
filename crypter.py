import random

lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
       'й', 'ц', 'у', 'к', 'е', 'н', 'ё', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',
       '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '&', '*', '%', '-', '_', '+', '=', '?', '.', ',', ' ']

lst2 = lst
hsh = {}
unhsh = {}
hsh_key = ''

for i in lst:
       a = random.choice(lst2)
       hsh[i] = a
       unhsh[a] = i
       lst2.remove(a)

for k, v in hsh.items():
       hsh_key = hsh_key + v

print('Try not to use it in Windows terminal!')
print('YOUR KEY IS:', hsh_key)
print('SAVE IT')

#===========================

n = input('Crypt/encrypt(c/e)?: ')

if n == 'c':
       n = input('File or text(f/t)?: ')

       if n == 't':
              n = input('Input text: ')
              n = n.lower()
       elif n == 'f':
              n = input("Ful path to file: ")
              file = open(n, 'r')
              n = file.read()
              file.close()
       else:
              print('BAD!!!')
              exit()

       for i in n:
              if i not in lst:
                     n = n.replace(i, '')
              else:
                     n = n.replace(i, hsh[i], 1)

       try:
              file = open('crypted.txt', 'x')
              file.close()
              file = open('crypted.txt', 'w')
              file.write(n)
              file.close()
       except:
              file = open('crypted.txt', 'w')
              file.write(n)
              file.close()

       print(f'Text saved to crypted.txt\nOutput: {n}')

elif n == 'e':
       hsh_key = input('Your key: ')
       unhsh = {}
       c = 0

       n = input('File or text(f/t)?: ')

       if n == 't':
              n = input('Input text: ')
              n = n.lower()
       elif n == 'f':
              n = input("Full path file: ")
              file = open(n, 'r')
              n = file.read()
              file.close()
       else:
              print('BAD!!!')
              exit()

       for i in lst:
              if hsh_key[c] not in lst:
                     hsh_key = hsh_key.replace(hsh_key[c], '')
              else:
                     unhsh[hsh_key[c]] = i
                     c += 1

       for i in n:
              if i not in lst:
                     n = n.replace(i, '')
              else:
                     n = n.replace(i, unhsh[i], 1)

       try:
              file = open('encrypted.txt', 'x')
              file.close()
              file = open('encrypted.txt', 'w')
              file.write(n)
              file.close()
       except:
              file = open('encrypted.txt', 'w')
              file.write(n)
              file.close()

       print(f'Text saved to encrypted.txt\nOutput: {n}')

else:
       print('BAD!!!')