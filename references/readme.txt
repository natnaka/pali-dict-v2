# encoding: utf-8
Table ที่สำคัญกับเรา 4 table คือ vocabulary, meaning, detailVocabularyMeaningMap, และ vocabMeanInSentence
2 อันแรก จะ map จากคำ บาลี -> int และ คำแปลไทย -> int
เนื่องจากบาลีคำหนึ่ง แปลไทยได้หลายคำ  ข้อมูลนี้จะถูกเก็บใน table 3 = detailVocabularyMeaningMap ในลักษณะ 1-to-many
ส่วน table ที่ 4 เราจะได้ frequency ด้วย คือจะบอกเลยว่า ในประโยคนี้-คำบาลีคำนี้ ใช้คำแปลว่าอะไร   ซึ่งจะทำให้เราดูได้ว่า คำแปลไหน มีความน่าจะเป็นสูงสุด
