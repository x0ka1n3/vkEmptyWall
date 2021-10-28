import vk, sys, time
v = 5.131

def progressBar(done, length, barLen = 20, title = ""):
	barFillNum = int(round(barLen*done/float(length)))
	barFill = barFillNum*"*"
	barRemain = (barLen - barFillNum)*"-"

	if len(title):
		title = "| " + title

	bar = barFill+barRemain
	barPerc = round((done/length)*100)
	sys.stdout.write("\r[%s] %d%s | %d/%d %s" % (bar, barPerc, "%", done, length, title))
	sys.stdout.flush()
	if done == length:
		print("\n")

access_token = "" # Вставить токен ВК

api = vk.API(vk.Session(access_token = access_token))

code = """var id, out = {"n":0, "post_ids":[] }, ids = API.wall.get({"count":24}).items@.id;out.post_ids = ids;while(id = ids.pop()) {API.wall.delete({"post_id":id});out.n = out.n + 1;}return out;"""

while True:
	api.execute(code = code, v = v)
	time.sleep(1.5)