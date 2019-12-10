# - Git **bash** work-flow

> pwd : 현재 Directory
>
> ls : list (folder: blue; file: gray)
>
> cd : change Directory
>
> cd / 
>
> cd ~
>
> .. : 상위 folder
>
> ---
>
> tap : 자동완성
>
> makdir : make Directory
>
> ls -a : 숨긴 것도 보여줘
>
> ---
>
> git init : **master** , Repositories in git 
>
> rm 파일명 : 삭제
>
> rm .git      ->      rm -rf .git    : master 떼기
>
> ---
>
> git status : 상태 확인
>
> git config --global user.email "가입한 이메일"   : 계정 연결
>
> git config --global user.name "이름"  
>
> ---
>
> git log
>
> git log --oneline
>
> Q : 명령 메시지 (master) 창으로 불러옴
>
> ---
>
> git remote add origin **Repositories adress**
>
> git remote -v  : 확인





# - Git **Push & Pull** work-flow

>mkdir house : new 'house' folder 
>
>cd house : change 'house' directory 
>
>git clone **Repositories adress**
>
>touch homework.txt  : new 'homwork.txt' in 'house' folder
>
>---
>
>git log : log(기록) check
>
>git log oneline : log check 1 line
>
>git log -1 : 마지막 하나만 보는 법
>
>
>
>| **Campus**  | **Github** | **House**   |
>| ----------- | ---------- | ----------- |
>| Push & Pull | Save       | Push & Pull |
>
>```bash
>git add .
># git file's name
>
>git commit -m "commit messages"
>git push
># git push origin master
>```
>
>```bash
>git status
># 항상 깨끗한 상태에서 pull 하기
>
>git pull origin master
># clone: 맨 처음만!
># Pull
>```
>
>```bash
>git diff 
># 파일 수정사항 확인하기
>```
>
>```bash
>cat file.txt
># 내용 볼 수 있음
>```





# - **SLACK** start !

 