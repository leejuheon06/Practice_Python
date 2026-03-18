print("Hello Github!")
print("Amazing!")


# - 설정
# git config --global user.name "Name"
# git config --global user.email "Email"

# 1. 시작
# git init
# git remote add origin **GitHub URL**
# 2. 파일 담기(add)
# git add .
# git add . -f      # ignore 파일 및 삭제한 파일 이력까지 커밋
# 3. 기록 (commit)
# git commit -m "로그 기록"             ex) "코드 수정 및 함수 업데이트"
# git commit --amend -m "로그 기록"     기존의 마지막 커밋을 수정하여 덮어쓰기
# 4. 업로드 (push)
# git push -u origin main     # 최초 업로드 실행 시
# git push                    # 이후 업로드 시

# - Git 설정값 리스트 확인
# git config --list

# - Git 저장소의 상태 확인
# git status

# - master >> main 변경
# git branch -m master main

# - 연결된 GitHub 저장소 해제
# git remote remove origin

# - origin에 remote 주소가 잘 등록되었는지 확인
# git remote show origin 

# - GitHub 최신 상태를 내 컴퓨터로 가져오기
# git fetch origin        # 협업 시 코드가 섞이지 않게 최신 업데이트 내용 사전 확인

# - 최신 상태 내용 합치기
# git merge origin/main   # 확인 후 수동으로 코드 합치기

# - 위 2개의 기능 동시 실행
# git pull                # 자동으로 코드 합치기, 사전 확인 불가로 코드가 섞일 수 있음

# - 예전 버전 롤백 적용
# git reset HEAD^ --soft
# HEAD : 현재위치 기준 상대적인 위치 설정, HEAD 확인시 get reflog 명령 이용
# --soft 옵션 : 기존의 인덱스와 워킹트리 보존하며 롤백
# --hard 옵션 : 기존의 인덱스와 워킹트리 버리고 롤백
# --mixed 옵션 : 기존의 인덱스는 버리고 워킹트리만 보존하며 롤백
# ^ : 바로 이전 단계
# ~2 : 바로 두번째 전 단계

# branch (브랜치)
# 원래의 코드 줄기는 그대로 두고 똑같은 복사본을 만들어 거기서만 코드를 수정하는 기능
# main (기존) : 완벽하게 실행 가능한 상태의 코드
# new (신규) : 기능을 추가하거나 실험해보고 싶은 "임시 작업 공간"

# 활용 이유
# 1. 메인 코드 보호
# 2. 동시 작업 가능
# 3. 버전 관리

# 활용 예시
# 1. 새 브렌치 만들기
# git branch new
# 2. 새 브렌치 이동
# git checkout new or git switch new
# <참고> git checkout -b new     # 생성과 이동을 동시에 진행
# 3. 작업 후 합치기
# git checkout main   # 메인으로 돌아오기
# git merge new       # new 브렌치의 내용 가져오기
# 4. 다 쓴 브렌치 삭제
# git branch -d new