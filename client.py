import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
image_data = xmlrpclib.Binary(open('test_image.jpg').read())
# url = "http://mmbiz.qpic.cn/mmbiz_jpg/YnnndYgX6CibQ8kgxLcNDmakc2WAyRdw9ye6vrWVCFZZMAwNylOFgF4gV1BKCLoT5hdugS7KvjcsElnic7zVIiclg/0"

print "3 is even: %s" % str(proxy.get_score(image_data))
