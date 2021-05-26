# PyHondt
Python script that calculates the number of seats according to the D'Hondt method.

## Prerequisites
* python
* csv
<br>
You don't need to do anything since csv module is included in the Python installation.

## Usage
1. Fill the columns after the "seats" column with the name of all parties.
2. If seats are reserved for constituencies, write the names of constituencies to the first column of each row except the first row. Otherwise, you can handle all the results in one constituency and name it "x".
3. If a party did not nominate a candidate in a constituency or did not receive votes, write 0 there. (Do not leave it blank!)
   ```sh
   npm install
   ```
4. Run the `main.py` file.
   ```sh
   python main.py
   ```

## Special notes on Turkish election system:
  - İttifak sistemi dünyada eşi bulunmayan bir sistem olduğu için Türkiye'deki seçim sonuçlarıyla karşılaştırdığınızda minör farklılıklar görebilirsiniz. Tam doğru sonuç almak için ittifakların toplam oyunu girip, ittifakın koltuk sayısını elde ettikten sonra D'Hondt sistemini ittifak içerisindeki partilerde çalıştırırsanız doğru sonuca ulaşırsınız.
  - sample_input.csv dosyasındaki bölgeler ve koltuk sayıları Mart 2021 tarihli YSK kararından alınmıştır. Zaman içerisinde nüfus değişimine göre değişiklik gösterebilir.
