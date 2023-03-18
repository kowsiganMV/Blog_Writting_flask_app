from pymongo import MongoClient

client=MongoClient("---db link-----")

db = client.get_database('flask_db')

records = db.login_records
img=db.img
posts=db.Posts
def adding(name,email,password):
      d=img.find()
      i=0
      for data in d:
            id=data['id']
            i+=int(id)
      
      up={'id' : str(i)}
      update={"$set" :{'id' : str(i+1)}}
      img.update_one(up,update)
      data={'_id' : str(i) ,
            'username' : name,
            'email' : email,
            'password' : password}
      records.insert_one(data)
      return i

def addpost(id,tittle,content,aurthor,date):
      d=img.find()

      i=0
      for data in d:
            post_id=data['post_ids']
            i+=int(post_id)
      
      up={'post_ids' : str(i)}
      update={"$set" :{'post_ids' : str(i+1)}}
      img.update_one(up,update)
      data={'id' : str(id), 
            'tittle' : tittle,
            'content' : content,
            'aurthor' : aurthor,
            'date' : date,
            'post_id' : str(i) }
      posts.insert_one(data)

def getdatas():
      d=records.find()
      datas=[]
      for data in d:
            id=data['_id']
            username=data['username']
            email=data['email']
            password=data['password']
            temp=[id,username,email,password]
            datas.append(temp)
      return datas

def get_posts():
      d=posts.find()
      postdata=[]
      for post in d:
            id=post['id']
            tittle=post['tittle']
            content=post['content']
            author=post['aurthor']
            date=post['date']
            temp=[id,tittle,content,author,date]
            postdata.append(temp)
      return postdata

def myblogs(id):
      posts=get_posts()
      my_posts=[]
      for post in posts:
            if post[0]==id:
                  my_posts.append(post)
      return my_posts
