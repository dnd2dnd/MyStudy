# Git
## Git/GitHub
- Git : 버전 컨트롤 시스템
- GitHub : 원격 저장소

<br>

## Git 사용
### 기본 세팅
git init - Git 저장소를 새로 만드는 명령

<br>

GitHub push용 이름 및 이메일 세팅 
```
$ git config --global user.name "username"
$ git config --global user.email "email@email.com"
```
--global 옵션은 default로 전체 깃 적용

<br>

Git 원격저장소와 연결 
```
git remote add origin [REPOSITORY ADDRESS]
```

<br>

파일 올리기
```
$ git add (파일명) // 특정 파일 stage에 추가
$ git add .        // 모든 파일 stage에 추가
$ git commit -m "(설명)" // local repository에 설명 추가
$ git push origin master // 로컬 저장소의 내용을 원격 저장소에 반영
```

<br>

상태 확인
```
$ git --version // 버전 확인
$ git log       // 커밋 이력 확인
$ git remote -v // 원격 저장소 확인
$ git staus     // stage 파일 상태 확인
```

<br>

### branch
```
$ git branch                // local 브랜치 확인
$ git branch                // remote 까지 확인
$ git branch (브랜치명)     // 브랜치 생성
$ git checkout (브랜치명)   // 해당 브랜치로 이동
$ git checkout -b (브랜치명)// 현재 커밋에서 브랜치 생성 후 이동
$ git branch -d (브랜치명)  // 로컬 저장소에서 브랜치 삭제
$ git push origin --delete (브랜치명) // 원격 저장소에서 브랜치 삭제
$git branch -m (현재 브랜치명) (바꿀 브랜치명) // 브랜치명 변경
```

<br>

### reset
로컬 저장소에서 이전 커밋으로 돌아가고 이후 커밋은 unstage상태로 만들기
```
$ git reset (커밋 아이디)
$ git reset HEAD^   // 한 커밋 이전 (^개수만큼 이전)
$ git reset --hard (커밋 아이디)
$ git reset --hard HEAD^
```

<br>

### 코드 가져오기
```
$ git pull origin main // 원격 저장소 main 가져오기
$ git clone (url)      // 원격 저장소 가져오기
$ git merge (브랜치명) // 브랜치를 병합
``` 
