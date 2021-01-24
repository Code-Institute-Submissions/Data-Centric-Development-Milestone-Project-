import os

# The name of your Mongo database.
os.environ['MONGODB_NAME'] = 'reviewdb'

# The Mongo URI
os.environ['MONGO_URI'] = ('mongodb+srv://root:70AoSLdgfRWWrOE6'
                           '@myfirstcluster.w2rzj.mongodb.net/reviewdb'
                           '?retryWrites=true&w=majority')
