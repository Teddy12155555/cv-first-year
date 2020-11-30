# VIPLab 碩一培訓手冊

## 每週進度

- [x] Week0 進度(11/25)前做完，用 Slack 傳給我就好

  > 寫一份 CV（英文較佳），可以用 [Cakeresume](https://www.cakeresume.com/resumes?ref=navs_resume_samples) 做

- [x] Week1 進度(11/30)做完

  > 首先下載這個影片(影片格式為 .mp4)：[小松菜奈が全力疾走！　映画「恋は雨上がりのように」主題歌「フロントメモリー」MV が公開](https://www.youtube.com/watch?v=ygNKQzKwXKM)
  >
  > 功能需求：
  > Python - opencv 讀取上面的影片
  > 使用 dlib 函式庫去擷取人臉
  > 並將 bounding box 畫在人臉上
  > 輸出影片 .mp4
  > 然後我會看程式碼，
  > 要做簡報(裡面放你的環境安裝步驟，程式碼介紹，成果展示)
  >
  > Advanced:
  > 如果將影片解析度調小或是調大，
  > 會比較容易框出人臉嗎？或是反而失敗了？

- [ ] Week2 進度(12/07)做完 ---- 有點難，請先做

  > [YOLO](https://arxiv.org/pdf/1506.02640.pdf)
  > 讀完論文、做簡報、寫一篇簡介。
  > 呵 認真寫喔 我會叫你們發佈到 Medium 喔。
  > 然後我會問問題，
  > 你們如果只看中文簡介然後不去看程式碼，
  > 你們一定會被我問倒。
  >
  > 每個人都說他看過 Yolo，
  > 每個人都說他會用，
  > 但 9 成的人明明什麼都不懂，
  > 如果只看中文/英文簡介的人，
  > 能理解的有限，
  > 因為寫的人其實不懂，
  > 但他們卻以為自己懂了。
  > 我們雖然不見得能成為最頂尖的人，
  > 但至少也要有一點水準，讓別人知道你的價值。

- [ ] Week3 進度(12/07) - 這其實會有很多工程面上的難點

  > 結合 Webcam(視訊頭，沒有的話來 TR-619 拿)進行即時的人臉偵測（OpenCV Dlib）
  > 並且利用 OpenCV 的 GUI 在人臉的部分畫出 Bounding box
  > 接著將上述的作業以及 Week1 的作業在 Docker 上面運行(這其實有難度)

- [ ] Week4 進度

  > YOLO v2，同 Yolo v1 之要求。

- [ ] Week5 進度
  > 選定一張臉，透過 Opencv 換臉，並可依照臉部進行轉換
  > OpenCV + Dlib(landmark) + Affine Transform
