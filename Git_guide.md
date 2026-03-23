# Git 실전 가이드북

## Phase 1. 초기 설정 (Setup)
* 사용자 등록 : 내 이름과 이메일로 커밋 기록을 남깁니다.
git config --global user.name "leejuheon06"
git config --global user.email "your-email@example.com"

## Phase 2. 브랜치(Branch)
메인 코드(main)를 망가뜨리지 않고 마음껏 실험하는 기능입니다.
* 새 브랜치 만들기 & 이동: git checkout -b feature/algo-test
* 브랜치 목록 보기: git branch (현재 있는 곳은 별표* 표시)
* 메인으로 돌아가기: git checkout main
* 브랜치 합치기: (메인에서 실행) git merge feature/algo-test

## Phase 3. 소스 업데이트 (Fetch vs Pull)
서버(GitHub)의 내용을 내 컴퓨터로 가져오는 두 가지 방법입니다.
* git fetch: 서버의 변화를 "확인만" 합니다. 내 코드는 바뀌지 않습니다. (신중파)
* git pull: 서버 내용을 가져와서 내 코드와 "바로 합칩니다". (속도파)
    * 강력 추천: git pull --rebase origin main (내 작업을 뒤로 밀고 서버 내용을 먼저 깔아줍니다. 히스토리가 훨씬 깨끗해집니다.)

## Phase 4. 소스 복원 (Restore & Reset)
* 저장 전 상태로 (파일 복원): git restore 파일명방금 수정한 내용을 다 지우고 마지막 커밋 상태로 돌아갑니다.
* 장바구니에서 빼기 (Unstage): git restore --staged 파일명add는 했지만 commit은 하기 싫을 때 사용합니다.
* 커밋 취소하기 (Reset):
    * git reset --soft HEAD~1: 방금 한 커밋만 취소하고, 내가 짠 코드는 그대로 둡니다. (다시 커밋할 때 좋음)
    * git reset --hard HEAD~1: 방금 한 커밋과 코드 수정을 모두 삭제합니다. (주의해서 사용!)

## Phase 5. 과거 수정 (Rebase) & 충돌 (Conflict)
1) 과거 커밋 내용 고치기
git rebase -i HEAD~5              # 1. 목록 열고 수정할 커밋 pick -> edit 변경
(파일 수정 후)
git add .                         # 2. 수정한 파일 담기
git commit --amend --no-edit      # 3. 과거 커밋에 덮어쓰기
git rebase --continue             # 4. 현재로 돌아오기
git push origin main --force      # 5. 서버에 강제 반영

2) 충돌 해결 루틴
* 발견: CONFLICT 메시지가 뜨면 VS Code에서 해당 파일을 엽니다.
* 해결: Accept Both Changes 버튼을 눌러 코드를 합치고 저장합니다.
* 마무리: git add . -> git rebase --continue

## Phase 6. '황금 루틴' (Daily Routine)
1) git pull --rebase origin main 시작 전 최신 상태 맞추기
2) 파일 수정 및 저장(Ctrl + S)
3) git add .                     모든 파일 담기
4) git commit -m "Day X: 주제"    기록 남기기
5) git push origin mainGitHub    저장소로 발송!