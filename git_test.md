1. Git基本
	- Git config設定
		1. git config --global user.name "XXXX"
		2. git config --global user.email "XXXX@mail.com"  

2. ローカルファイルをプッシュ
    - git init
    - git add .
    - git commit -m "Initial commit"
    - git remote add origin https://github.com/XXXX/XXXX.git
    - git push -u origin master

3. リモートから変更を取得
    - git pull

4. ローカルの変更を確認する, addされているかを確認できる。
    - git status

5. リモートとローカルのファイルの差分を抽出する。
    - git diff <filename>

6. コミットの変更履歴を見る
    - git log

7. コミットの変更点を見る
    - git show <コミットのハッシュ値>

8. リモートにプッシュ
    - git push origin <ブランチ名>

9. addの取り消し
    - git reset HEAD <ファイル名>

10. commitの取り消し
    - git revert <commit ハッシュ値> -n

11. pushの取り消し
    - git reset --hard <commit ハッシュ値>
    - git push -f

12. ローカルでブランチを作成
    - git branch <ブランチ名>

13. ローカルでブランチを切り替え
    - git checkout <ブランチ名>

14. ローカルでブランチ作成 & 切り替え
    - git checkout -b <ブランチ名> 

15. ローカルのブランチを反映させる
    - git push -u origin <ブランチ名>

16. リモートのブランチをローカルに持ってくる & 切り替え
    - git branch <ブランチ名> origin/<ブランチ名>

17. ブランチを比較
    - git diff <ブランチ名> <ブランチ名>

18. マージ
    - git checkout <合流先のブランチ名>
    - git pull 
    - git merge <合流するブランチ名>
    - git add .
    - git commit -m "test"
    - git push origin <合流先のブランチ名>

19. 変更点を一時退避
    - git stash save

20. 退避した作業のリストを作成
    - git stash list

21. 退避した作業を戻す
    - git stash apply <stash名>

22. 退避した作業を消す
    - git stasj drop <stash名>

23. ファイル削除
    - git rm -f <ファイル名>
    
24. ファイルリネーム
    - git mv <元のファイル> <変更後ファイル名>

25. ファイルを最新のコミットの状態に戻す
    - git checkout HEAD <ファイル名>

26. ファイルを指定コミットまで戻す.
    - git checkout <コミットのハッシュ値> <ファイル名>

27. .gitignoreを無視して追加
    - git add -f <ファイル>