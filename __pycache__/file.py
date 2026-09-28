import csv

def save_to_csv(jobs):
    # 'opne'을 'open'으로 수정
    with open("downloads.csv", "w", encoding="cp949", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No", "회사", "제목", "지역", "상세보기"])
        
        for index, job in enumerate(jobs):
            csv_writer.writerow([
                index + 1,               # 1 대신 index + 1 사용
                job["company"],
                job["title"],
                job["location"],         # <- 쉼표(,) 추가됨
                job["link"]
            ])