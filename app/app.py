from fastapi import FastAPI ,HTTPException

app=FastAPI()
text_post={ 1:{"title":"DEMO POST","Content":"Demo Content"},
    2: {
        "title": "Second Demo Post",
        "content": "This is the content of the second demo post."},
            3: {
        "title": "Third Demo Post",
        "content": "This is the content of the third demo post."
    },
    4: {
        "title": "Fourth Demo Post",
        "content": "This is the content of the fourth demo post."
    },
    5: {
        "title": "Fifth Demo Post",
        "content": "This is the content of the fifth demo post."
    },
    6: {
        "title": "Sixth Demo Post",
        "content": "This is the content of the sixth demo post."
    },
    7: {
        "title": "Seventh Demo Post",
        "content": "This is the content of the seventh demo post."
    },
    8: {
        "title": "Eighth Demo Post",
        "content": "This is the content of the eighth demo post."
    },
    9: {
        "title": "Ninth Demo Post",
        "content": "This is the content of the ninth demo post."
    },
    10: {
        "title": "Tenth Demo Post",
        "content": "This is the content of the tenth demo post."
    }
}

@app.get("/posts")
def get_all_posts():
    return text_post
@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_post:
        raise HTTPException(status_code=404,detail="Post not found")
    return  text_post.get(id)