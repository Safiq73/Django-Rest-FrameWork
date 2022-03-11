# from rest_framework.pagination import PageNumberPagination

# class MyPage(PageNumberPagination):
#     page_size=5     # this for mentioning page size
#     page_query_param = 'p'  #http://127.0.0.1:8000/paginationn/?p=3  here url will change from page=3 to p=3 basically to change the string
#     page_size_query_param = 'records' #http://127.0.0.1:8000/paginationn/?records=9   #Here user mentioning how many records to show in each page
#     max_page_size = 10          # http://127.0.0.1:8000/paginationn/?records=11   # Max number of records in each page, If user given more than this it will show only max_page_size
#     # last_page_strings = 'Akhir'  

# from rest_framework.pagination import LimitOffsetPagination

# class MyPage(LimitOffsetPagination):
#     default_limit=5     # this for mentioning default limit if there is not limit mentioned
#     limit_query_param = 'mylim'  #http://127.0.0.1:8000/paginationn/?limit=3  here url will change from limit=3 to mylimit=3 basically to change the string
#     offset_query_param = 'myoffset' #http://127.0.0.1:8000/paginationn/?myoffset=9   #here url will change from offset=3 to myoffset=3 basically to change the string
#     max_limit = 10          # http://127.0.0.1:8000/paginationn/?limit=11   # Max number of records in each page, If user given more than this it will show only max_page_size
    

from rest_framework.pagination import CursorPagination

class MyPage(CursorPagination):
    page_size=5     # this for mentioning number of records in a page, 
    ordering = 'first_name'  # here we are changing the ordering from timestamp to first_name
    # cursor_query_param = 'mycursor'  # /?cursor=bz0xJnA9QmFycmll&page=12 here url will change from cursor=3 to mycursor=3 basically to change the string
   