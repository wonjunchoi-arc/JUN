'''
이름,전화번호,이메일,주소를 받아서 연락처 입력,출력,삭제하는 프로그램을 완성하시오.
'''


class Contacts(object):
    def __init__(self, name, phone, mail, address):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address

    def get_Contacts(self):
        return f'주소록 : 이름 {self.name}, 전화번호{self.phone}, 메일은 {self.mail}, 주소는 {self.address}'




    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]


    @staticmethod
    def main():
       ls = []
       while 1:
           menu =input('0. Exit 1.입력 2. 출력 3.수정 4.삭제')
           if menu == '0':
               break
           elif menu == '1':
               ls.append(Contacts(input('이름'), input('전화번호'), input('메일'), input('주소'))) # ls.append는 뒤의 것들을 리스트 안에 넣겠다는 소리다.

           elif menu == '2':
               for i in ls:
                   print(f'출력결과: {i.get_Contacts()}')


           elif menu == '3':
                edit_name = input('수정할 내용:')
                contacts.del_element(ls, name)
                contackts = Contacts(input("이름"),input("전화번호"),input("메일"),input("주소"))
                ls.append(Contacts)



           elif menu == '4':
               del_name = input('삭제할 이름')



           else:
               print('잘못된 주문 입니다')
               continue





Contacts.main()

