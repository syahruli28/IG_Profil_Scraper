from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
import csv
import time

class InstaCrawl:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome("C:/Users/acer/Downloads/chromedriver.exe")
        content = self.bot.page_source
        # self.soup = BeautifulSoup(content, 'html.parser')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def get_tags(self,tag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+ tag +'/')
        time.sleep(4)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
            insta = bot.find_elements_by_css_selector('.v1Nh3.kIKUG._bz0w')
            elems = bot.find_elements_by_css_selector('.v1Nh3.kIKUG._bz0w [href]')
            links = [elem.get_attribute('href') for elem in elems]
            u = 1
            for link in links:
                bot.get(link)
                print('Like ke :'+ str(u))
                u = u+1
                try:
                    bot.find_element_by_class_name('_8-yf5').click()
                    time.sleep(3)
                except Exception as e:
                    time.sleep(3)
    
    def crawl_profil(self,profil):
        bot = self.bot
        # soup = self.soup
        bot.get('https://www.instagram.com/'+ profil +'/')
        time.sleep(2)

        # # persiapan membuat file csv dan menambahkan headernya
        f = csv.writer(open(profil+'.csv', 'w', newline='\n'))
        header = ['Nama', 'Caption & Hashtag', 'URL Image', 'Tanggal Post']
        f.writerow(header)
        # asal
        nama = 'Nama'
        caption = 'Caption & Hashtag'
        urlimage = 'URL Image'
        date = 'Tanggal Post'
        # buka file csv yang telah dibuat sebelumnya
        bukacsv = open(profil+'.csv', 'a', newline='\n')
        save = csv.writer(bukacsv)
        save.writerow([nama, caption, urlimage, date])

        # /html/body/div[4]/div[1]/div/div/a
        # /html/body/div[4]/div[1]/div/div/a[2]
        # looping = bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
        # buat variabel untuk perulangannya
        total_post = bot.find_element_by_class_name('g47SY')
        rawpost = total_post.text

        # cek apakah ada koma pada total postnya
        if ',' in rawpost:
            rawpost = rawpost.replace(',','')
            post = int(rawpost)
        else:
            post = int(rawpost)

        print('Terdapat '+str(post)+ ' total post.')
        
        # cek kondisi untuk perulangan
        if post > 2:
            print('Melakukan perulangan sebanyak '+str(post))
        elif post > 1:
            print('Melakukan perulangan sebanyak '+str(post))
        else:
            print('Melakukan perulangan sebanyak '+str(post))

        print('MEMULAI PROSES CRAWLING...')
        u = 0

        # cek kondisi bila post lebih dari 2 atau tidak
        # kalau post lebih dari 3
        if post > 2:    
            fcard = bot.find_element_by_css_selector('.v1Nh3.kIKUG._bz0w')
            acard = fcard.find_element_by_tag_name('a')
            acard.click()
            time.sleep(4)
            # crawl data url, nama, caption dan tanggal
            # post pertama
            try:
                urlimage = bot.current_url
                # rrawcaption = bot.find_element_by_css_selector('.C4VMK')
                rawcaption = bot.find_element_by_class_name('C4VMK')
                rcaption = rawcaption.text
                rcaption = rcaption.replace(profil, '')
                rawdate = bot.find_element_by_tag_name('time')
                nama = profil
                caption = rcaption
                date = rawdate.get_attribute('title') 
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            except Exception as e:
                urlimage = bot.current_url
                nama = profil
                caption = 'Tidak ada'
                date = 'Tidak ada' 
                print('Ada kesalahan : '+str(e))
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')

            # buka file csv yang telah dibuat sebelumnya
            bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
            save = csv.writer(bukacsv)
            save.writerow([nama, caption, urlimage, date])

            # tambahkan variabel u
            u+= 1

            # lanjut ke post selanjutnya
            button_next = bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            button_next.click()
            time.sleep(4)

            # post kedua
            try:
                urlimage = bot.current_url
                rawcaption = bot.find_element_by_class_name('C4VMK')
                rcaption = rawcaption.text
                rcaption = rcaption.replace(profil, '')
                rawdate = bot.find_element_by_tag_name('time')
                nama = profil
                caption = rcaption
                date = rawdate.get_attribute('title') 
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            except Exception as e:
                urlimage = bot.current_url
                nama = profil
                caption = 'Tidak ada'
                date = 'Tidak ada' 
                print('Ada kesalahan : '+str(e))
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            
            # buka file csv yang telah dibuat sebelumnya
            bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
            save = csv.writer(bukacsv)
            save.writerow([nama, caption, urlimage, date])

            # tambahkan variabel u
            u+= 1

            # u = 2
            while ( u < post ):
                # lanjut ke post selanjutnya
                button_next = bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                button_next.click()
                time.sleep(4)

                # post seterusnya
                try:
                    urlimage = bot.current_url
                    rawcaption = bot.find_element_by_class_name('C4VMK')
                    rcaption = rawcaption.text
                    rcaption = rcaption.replace(profil, '')
                    rawdate = bot.find_element_by_tag_name('time')
                    nama = profil
                    caption = rcaption
                    date = rawdate.get_attribute('title') 
                    print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
                except Exception as e:
                    urlimage = bot.current_url
                    nama = profil
                    caption = 'Tidak ada'
                    date = 'Tidak ada' 
                    print('Ada kesalahan : '+str(e))
                    print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
                
                # buka file csv yang telah dibuat sebelumnya
                bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
                save = csv.writer(bukacsv)
                save.writerow([nama, caption, urlimage, date])
                u+= 1
        
        # kondisi kalau post ada 2
        elif post == 2:
            fcard = bot.find_element_by_css_selector('.v1Nh3.kIKUG._bz0w')
            acard = fcard.find_element_by_tag_name('a')
            acard.click()
            time.sleep(4)
            # crawl data url, nama, caption dan tanggal
            # post pertama
            try:
                urlimage = bot.current_url
                rawcaption = bot.find_element_by_class_name('C4VMK')
                rcaption = rawcaption.text
                rcaption = rcaption.replace(profil, '')
                rawdate = bot.find_element_by_tag_name('time')
                nama = profil
                caption = rcaption
                date = rawdate.get_attribute('title') 
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            except Exception as e:
                urlimage = bot.current_url
                nama = profil
                caption = 'Tidak ada'
                date = 'Tidak ada' 
                print('Ada kesalahan : '+str(e))
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')

            # buka file csv yang telah dibuat sebelumnya
            bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
            save = csv.writer(bukacsv)
            save.writerow([nama, caption, urlimage, date])

            # tambahkan variabel u
            u+= 1

            # lanjut ke post selanjutnya
            button_next = bot.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            button_next.click()
            time.sleep(4)

            # post kedua
            try:
                urlimage = bot.current_url
                rawcaption = bot.find_element_by_class_name('C4VMK')
                rcaption = rawcaption.text
                rcaption = rcaption.replace(profil, '')
                rawdate = bot.find_element_by_tag_name('time')
                nama = profil
                caption = rcaption
                date = rawdate.get_attribute('title') 
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            except Exception as e:
                urlimage = bot.current_url
                nama = profil
                caption = 'Tidak ada'
                date = 'Tidak ada' 
                print('Ada kesalahan : '+str(e))
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            
            # buka file csv yang telah dibuat sebelumnya
            bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
            save = csv.writer(bukacsv)
            save.writerow([nama, caption, urlimage, date])  

        # post = 1
        else:
            fcard = bot.find_element_by_css_selector('.v1Nh3.kIKUG._bz0w')
            acard = fcard.find_element_by_tag_name('a')
            acard.click()
            time.sleep(4)
            # crawl data url, nama, caption dan tanggal
            # post pertama
            try:
                urlimage = bot.current_url
                rawcaption = bot.find_element_by_class_name('C4VMK')
                rcaption = rawcaption.text
                rcaption = rcaption.replace(profil, '')
                rawdate = bot.find_element_by_tag_name('time')
                nama = profil
                caption = rcaption
                date = rawdate.get_attribute('title') 
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')
            except Exception as e:
                urlimage = bot.current_url
                nama = profil
                caption = 'Tidak ada'
                date = 'Tidak ada' 
                print('Ada kesalahan : '+str(e))
                print('Data ke-'+str(u)+' telah ditambahkan ke '+str(profil)+'.csv, tersisa '+str(post-u)+' data lagi.')

            # buka file csv yang telah dibuat sebelumnya
            bukacsv = open(profil+'.csv', 'a', encoding='utf-8', newline='\n')
            save = csv.writer(bukacsv)
            save.writerow([nama, caption, urlimage, date])  

        time.sleep(2)
        bot.quit()
        pilihan = input('Apakah anda ingin pergi ke menu awal? (1=Ya, 2=Tidak) : ')
        if pilihan == '1':
            # pergi ke menu awal
            insta = InstaCrawl('081320375696','28051999')
            insta.login()
            insta.menu()
        elif pilihan == '2':
            print('Proses telah selesai.')
            quit('Keluar dari program')
        else:
            print('Input tidak diketahui.')
            quit('Keluar dari program')

    def find_profile_real_name(self,key):
        bot = self.bot
        time.sleep(3)
        search = bot.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.clear()
        search.send_keys(key)
        time.sleep(4)
        profiles = bot.find_elements_by_class_name('Ap253')
        u = 1
        for profile in profiles:
            # url
            print('{}. {}'.format(u, profile.text))
            u = u+1

        bot.quit()
        c = input('Apakah anda ingin men-crawl data dari salah satu akun yang telah dicari? (1=Ya, 2=Tidak) : ')
        if c == '1':
            key = input('Masukan nama akun : ')
            insta = InstaCrawl('081320375696','28051999')
            insta.login()
            insta.crawl_profil(key)
        elif c == '2':
            bot.quit()
            print('Proses crawl telah selesai.')
            quit('Keluar dari program')
        else:
            bot.quit()
            print('Input tidak diketahui')
            print('Proses crawl telah selesai.')
            quit('Keluar dari program')

    def menu(self):          
        bot = self.bot
        # Menu Awal
        print('=============================================')
        print('[1]. Sukai semua berdasarkan Hashtag [X]')
        print('[2]. Cari nama akun profil')
        print('[3]. Crawl data berdasarkan nama profil akun')
        print('[4]. Keluar')
        print('=============================================')

        bot.quit()
        time.sleep(2)
        # Pilih menu
        pilihan = input('Masukan pilihan menu ke : ')

        # pengkondisian menu pilihan
        if pilihan == '1':
            # menu crawl by hashtag
            print('=============================================')
            key = input('Masukan kata kunci : ')
            insta = InstaCrawl('081320375696','28051999')
            insta.login()
            insta.get_tags(key)
        elif pilihan == '2':
            # menu search IG account
            print('=============================================')
            key = input('Masukkan kata kunci : ')
            insta = InstaCrawl('081320375696','28051999')
            insta.login()
            insta.find_profile_real_name(key)
        elif pilihan == '3':
            # menu crawl by IG name account
            print('=============================================')
            key = input('Masukkan nama akun : ')
            insta = InstaCrawl('081320375696','28051999')
            insta.login()
            insta.crawl_profil(key)
        elif pilihan == '4':
            # menu Keluar
            print('=============================================')
            quit('Keluar dari program')
        else:
            print('Pilihan tidak diketahui!!')
            quit('Keluar dari program')

# Halaman Awal
insta = InstaCrawl('081320375696','28051999')
insta.login()
insta.menu()