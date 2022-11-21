from django.core.paginator import Paginator

obj = ["Tushar", "Himanshu", "Tarun", "Neelansh", "Aaditya", "Piyush", "Meghanshu"]

p = Paginator(obj, 2)

print(p.count)
print(p.num_pages)
print(p.page_range)
print(p.page(1))
print(p.page(2))