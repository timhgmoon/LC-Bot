**LC-Bot**
Tim
December, 2021
General Assembly

---

***Project Description***
- ✨ This app will be a blog post of coding questions/process of getting a job after general assembly.  Main focus of the app will be using a discord bot to send daily leetcode questions and being able to search questions/answers through discord using commands.

***Pages***
- *Landing Page*: List of blogs and short description under them. 
- *Add post*: Will make a new blog. 
- *About*: Short description of discord functions w/ commands and a description of current blog
- *Blog*: Will include blog post w/ ability to allow other users to add comments.

***User Stories***
- 🤔 Who are our users, what do they want, and why?
- Users are anybody that wants to join my journey looking for a job. Can also join discord to get daily(randomized) coding problems.

***Wire Frames***
- 📝 Sketches of views and interfaces in the application.
- Link to [initial idea, wireframes, and react architecture](https://imgur.com/a/BhcJbqE)
- Link to [snippet of discord bot-basic](https://imgur.com/rDvR1tX)

***Time/Priority Matrix***
📊 Table including functionality and estimated vs. actual time for completion. 

| Component | Priority | Estimated Time | Actual Time |
| --- | :---: | :---: | :---: |
| model schemas / CRUD| H |4hrs | 1hr |
| setting up gatsby/documentation| H | 1hr | 5hr |
| discord bot| H | 10hrs | 10hr |
| creating components(nav)| H | 1hrs | 1hrs |
| creating components(landing page)| H | 4hrs | 2hr |
| creating components(blog post page)| H | 2hrs | 6hr|
| creating components(about)| M | 3hrs | 1hr |
| connecting frontend w/ backend| H | 3hrs | 2hr(not finished) | 
| styling pages(mobile)| H| 5hrs | 1hr |
| styling pages(desktop)| H| 3hrs  | 4hr |
| animation | L | 2hrs | 0hrs |
| Total | x | 38hrs | 33hrs |

***MVP***
- Layout and Structure
- Models/database
- discord bot send coding question daily
- adding post for blog
- css(landing page, about, blog post, add blog)
- heroku upload

***POST-MVP***
- add timer to solve coding question
- add stackover flow api for easy access through discord
- read wagtail CMS documentation for django 
- search stackoverflow through my webpage?
- 
***Challenges*** 
-Discord interval function
- First tried to use a while loop that used a time.sleep() method but the other commands weren't working, reading through the documentation I found a built in method using @task.loop().
```
@tasks.loop(hours=12)
async def send_message():
    channel = client.get_channel(<enter channel id here>)
    new_url = GrabUrl.getUrl()
    await channel.send(new_url)
```

-Pagination
-Decided to use the built in bootstrap pagination but had to add a little bit of functionality to get it to work.
-Used this package documentation as a reference on how to build the structure(didn't use package)
[link](https://www.npmjs.com/package/react-paginate)
```
  const lastArticle = currentArticle * articlesPerPage
  const firstArticle = lastArticle - articlesPerPage
  const currentArticles = articles.slice(firstArticle, lastArticle)
  const pag = (pageNum) => {
    setCurrentArticle(pageNum)
  }
 ```
---
