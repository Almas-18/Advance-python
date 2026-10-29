#LIBRARY SYSTEM USING DATATYPES
books=[]
while True:
    print('==========Library systems==========')
    print('1. Add book')
    print('2. Issue book')
    print('3. Return book')
    print('4. Avaliable book')
    print('5. Display all book')
    print('6. Exit')

    ch=input('Enter your choice ::')

    if ch=='1':
        bid=  int(input('enter book id ::'))
        bname=input('enter book name::')
        author=input('enter book author::')

        book={
            'id':bid,
            'name':bname,
            'author':author,
            'issued':False
        }

        books.append(book)
        print('Book added successfully')
    elif ch=='2':
        bid=int(input('enter book id ::'))
        found=False

        for b in books:
            if b['id']==bid:
                found =True

                if b['issued']:
                    print('Book is already issued')
                else:
                    b['issued']=True
                    print('book is issued successfully')
                    break
            if not found:
                print('Book not found')
    elif ch=='3':
        bid=int(input('enter book id ::'))
        found= False

        for b in books:
            if b['id']==bid:
                found=True

                if not b['issued']:
                    print('book was not issued')
                else:
                    b['isuued']=False
                    print('Book returned successfully')
                    break

            if not found:
                print('Book not found')
    elif  ch == '4':
        print('=======Available Books======')
        avaiable= False

        for b in books:
            if not b['issued']:
                print(f'ID ::{b['id']}\t name::{b['name']}\tauthor::{b['author']}')
                available=True
            if not avaiable:
                print('book not avaiable')
    elif ch=='5':
        print('===Books====')
        if len(books)==0:
            print('No Books Found')
        else:
            for b in books:
                status="Issued" if b["issued"] else 'Available'
                print(f'ID ::{b['id']}\t name::{b['name']}\tauthor::{b['author']}\t status::{status}')
    elif ch=='6':
        print('Thank you for using our library')
        break
    else:
        print('invalid choice')