# PyHondt
Python script that calculates the number of seats according to the D'Hondt method.

## Prerequisites
* python
* csv
You don't need to do anything since csv module is included in the Python installation.

## Special notes on Turkish election system:
  - İttifak sistemi dünyada eşi bulunmayan bir sistem olduğu için Türkiye'deki seçim sonuçlarıyla karşılaştırdığınızda minör farklılıklar görebilirsiniz. Tam doğru sonuç almak için ittifakların toplam oyunu girip, ittifakın koltuk sayısını elde ettikten sonra D'Hondt sistemini ittifak içerisindeki partilerde çalıştırırsanız doğru sonuca ulaşırsınız.
  - sample_input.csv dosyasındaki bölgeler ve koltuk sayıları Mart 2021 tarihli YSK kararından alınmıştır. Zaman içerisinde nüfus değişimine göre değişiklik gösterebilir.
