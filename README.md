# About
**SudokuAreEz-SAT** adalah project yang mengaplikasikan _Satisfiability_ dalam _Propositional Logic_ (Matematika Diskrit) untuk menyelesaikan permainan [Sudoku](https://en.wikipedia.org/wiki/Sudoku) dengan bantuan komputer.

Project ini, merupakan sarana untuk menerapakan ilmu yang telah diperoleh **(Learning Purpose)**.

# Note To Reader
**Disaranakan** untuk menonaktifkan dark mode, ketika membaca [Project Notes](#project-notes)

Mohon maaf, jika pada bagian [Project Notes](#project-notes.) tidak menggunakan bahasa baku atau tidak se-utuhnya menggunakan bahasa Indonesia yang baik dan benar, dan tidak menjelaskan istilah-istilah Matematika serta jika terdapat kesalahan atau kekurangan dalam penjelasan.

# Project Notes
Logika Matematika adalah ilmu berfikir atau penalaran untuk menyimpulkan dan verifikasi dari sebuah statement.

***Contoh 1.1:*** \
Perhatikan statement matematika berikut, ![equation](https://latex.codecogs.com/gif.latex?\bg_white&space;\dpi{100}&space;\small&space;\forall&space;n,&space;n\in\mathbb{N}:\left[&space;P(n)&space;=&space;1&space;&plus;&space;2&space;&plus;&space;...&space;&plus;&space;n&space;=&space;\frac{n\left(n&space;&plus;&space;1\right)}{2}\right]) dimana ℕ adalah bilang asli (1, 2, 3, ... [Silahkan buka [_Discussions_](https://github.com/afifabroory/SudokuAreEz-SAT/discussions) baru di project ini untuk list lengkap bilangan bulat]).Statement tersebut adalah statement True.

Proof:\
(1) Statement True untuk n = 1, P(1) \
(2) n = k, Statement True untuk P(k) \
(3) Statement juga True untuk P(k + 1) \
Sehingga dapat disimpulkan bahwa statement tersebut adalah True ![equation](https://latex.codecogs.com/gif.latex?\bg_white&space;\dpi{100}&space;\small&space;\left&space;[&space;P(n)&space;\implies&space;P(n&space;&plus;&space;1)&space;\right&space;]).

Propositional Logic adalah cabang logika yang berkiatan dengan propositions. Propositions adalah statement yang memiliki _Truth Value_ diantara True dan False, sebuah proposition tidak dapat memiliki dua nilai Truth Value.

***Contoh 1.2:***\
(1) Indonesia Merdeka pada tahun 1945. Statement tersebut adalah True. \
(2) Bandung adalah ibu kota Amerika Serikat.  Statement tersebut adalah False :joy:. \
(3) Saya adalah orang Indonesia **atau** Saya adalah kuda. Statement tersebut adalah True karena saya adalah orang Indonesia, tidak peduli apakah saya kuda atau tidak :sweat_smile:, statement tersbut tetap True.
> ... (3) Saya adalah orang Indonesia **atau** Saya adalah kuda adalah contoh dari _compound proposition_ yang dihubungkan dengan [_logical connectives_](https://en.wikipedia.org/wiki/Logical_connective) atau operator logika (_i.e. Conjunction, Disjunction, Negation, Material Implication/Implies dan Bi-Implication_)

(4) x + 2 = 10. Statement tersebut **bukan** merupakan propositions, dikarenakan _Truth Value_ tersebut tergantung dengan nilai yang diberikan pada variable x.
> ... (4) Konsep ini dipelajari dalam [First-Order Logic (FOL)](https://en.wikipedia.org/wiki/First-order_logic) yang mana merupakan pelengkap kekurangan dari propositions logic, karena proposition logic tidak dapat merepresentasikan semua jenis Statement Matematika. Pada **Contoh 1.1** merupakan FOL, ketika sebuah nilai dari domain dimasukkan ke variable x pada _predicate function_ maka statement tersebut akan menjadi proposition.

Logika Matematika memegang peran dalam dunia Teknologi Informasi, sebagai contoh penerapan logika, yaitu pada:
- Arsitektur Komputer
- Program Verification dan Validation
- Artificial Intelligence
- Automated Theorem Proving
- dll.

Pada project ini akan menerapkan Logika Matematika dalam menyelesaikan permainan Sudoku.

<br>

[Sudoku](https://en.wikipedia.org/wiki/Sudoku) merupakan permainan _logic based_, dengan tujuan permainan adalah mengisi penuh semua _cell_ kosong dengan angka sesuai dengan jumlah _cell_ pada Sudoku (_e.g. Sudoku 9x9 maka mengisi angka 1-9_).

Pada Sudoku 9x9 terdapat kotak kecil dengan ukuran 3x3, yang mana pada kotak kecil 3x3 terdapat _cell_ kosong yang perlu disi penuh sesuai dengan syarat permainan Sudoku.
![Screenshot from 2021-03-07 16-26-00](https://user-images.githubusercontent.com/62495819/110233888-0b6ac000-7f62-11eb-90a6-f5dc70ae53bb.jpg) \
*Gambar 1.1: Contoh permainan Sudoku, dari Sudoku.com*

Syarat mengisi _cell_ kosong tersebut yaitu:
- Baris dan Kolom pada _cell_ kosong tersebut belum terdapat angka yang akan di masukkan (Baris dan kolom angkanya harus _unique_).
- Pada kotak kecil dibagian _cell_ yang kosong belum terdapat angka yang akan dimasukkan.

Namun, yang perlu diperhatikan dalam mengisi _cell_ kosong pada Sudoku adalah perhatikan lokasi angka atau kombinasi angka yang digunakan.

Terdapat berbagai macam teknik untuk menyelesaikan permaianan Sudoku dengan bantuan komputer, seperti Backtracking, SAT Problem, Stochastic search, dll. Pada project ini menggunakan teknik _Satisfiability (SAT) Problem_. SAT Problem dikategorikan di dalam [NP-Complete](https://en.wikipedia.org/wiki/NP-complete).

SAT Problem adalah problem yang menentukan apakah sebuah _Boolean Formula_ **Satisfiable** atau **Unsatisfiable**. Sebuah _formula_ X disebut satisfiable jika paling tidak terdapat nilai True, pada Truth Table. Sedangkan, sebuah _formula_ X adalah unsatisfiable jika dan hanya jika (iff) ¬X adalah Tautology atau dengan kata lain, X tidak memiliki truth value True sama sekali pada Truth Table.

***Contoh 1.3:*** \
(1) Misalkan, literal a adalah True sedangkan b adalah False. \
![proposition](https://latex.codecogs.com/gif.latex?\bg_white&space;\dpi{120}&space;\normal&space;\underbrace{(a&space;\wedge&space;\neg&space;b)}_\text{T}) \
Proposition diatas merupakan Satisfiable, karena terdapat truth value True, ketika a adalah True dan b adalah False.

(2) Misalkan literal a adalah True. \
![proposition](https://latex.codecogs.com/gif.latex?\bg_white&space;\dpi{120}&space;\normal&space;\underbrace{(a&space;\wedge&space;\neg&space;a)}_\text{F}) \
Proposition diatas merupakan Unsatisfiable, karena tidak terapat truth value True sekalipun pada Truth Table. Maka, negation dari compound proposition tersbeut adalah Tautology ![proposition](https://latex.codecogs.com/gif.latex?\bg_white&space;\neg(a&space;\wedge&space;\neg&space;b)&space;\leftrightarrow&space;\text{T})

Dalam SAT Problem, sebuah compound proposition harus dirubah ke dalam bentuk Conjunctive Normal Form (CNF). \
Fakta menarik dari CNF adalah semua proposition dapat dibentuk kedalam bentuk CNF.
> Every propositional formula can be converted into an equivalent formula that is in CNF. This transformation is based on rules about logical equivalences: double negation elimination, De Morgan's laws, and the distributive law. \
> [Conjunctive normal form (Wikipedia)](https://en.wikipedia.org/wiki/Conjunctive_normal_form#Conversion_into_CNF)

Sebuah _expression_ X dalam bentuk CNF jika memiliki pola atau diekspresikan sebagai Conjunction of Clauses, dimana Clauses adalah Disjunction of Literals (Conjunction Of Disjunction of Literals). \
***Contoh 1.4:*** \
Berikut adalah contoh-contoh _expression_ dalam bentuk CNF \
![cnf form 1](https://latex.codecogs.com/gif.latex?\bg_white%20\inline%20\dpi{150}%20\underbrace%20{%20\overbrace{(p%20\vee%20\neg%20q)}^\text{Disj.%20of%20Literals}%20\wedge%20\overbrace{(q%20\vee%20\neg%20r)}^\text{Disj.%20of%20Literals}%20\wedge%20\overbrace{(r%20\vee%20\neg%20p)}^\text{Disj.%20of%20Literals}%20}_\text{Conjunction%20of%20Clauses})

![cnf form 2](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cinline%20%5Cdpi%7B150%7D%20%28p%20%5Cvee%20%5Cneg%20q%29) Merupakan CNF, karena secara implisit terdapat Conjunction dengan clauses constant True. ![cnf form 2 equiv form](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cinline%20%5Cdpi%7B150%7D%20%28p%20%5Cvee%20%5Cneg%20q%29%20%5Cwedge%20%28T%20%5Cvee%20T%29) 
> Untuk contoh lebih, bisa dilihat di [Conjunctive Normal Form (Wikipedia)](https://en.wikipedia.org/wiki/Conjunctive_normal_form#Examples_and_non-examples)

**Algoritma untuk konversi bentuk propositional formula ke dalam bentuk CNF (sering digunakan):**
> 1) Merubah semua bi-implication [Jika ada] \
> ![bi-implication into logical equivalent form](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cdpi%7B150%7D%20p%20%5Cleftrightarrow%20q%20%5Cequiv%20%28p%20%5Crightarrow%20q%29%20%5Cwedge%20%28q%20%5Crightarrow%20p%29)
> 2) Merubah semua implication [Jika ada] \
> ![implcation into logical equivalent form](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cdpi%7B150%7D%20%28p%20%5Crightarrow%20q%29%20%5Cequiv%20%28%5Cneg%20p%20%5Cvee%20q%29)
> 3) Menerapakan De Morgan's Law [Jika bisa] \
> ![applying de morgan's law as you can](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cdpi%7B150%7D%20%5C%5C%20%5Cneg%28p%20%5Cwedge%20q%29%20%5Cequiv%20%28%5Cneg%20p%20%5Cvee%20%5Cneg%20q%29)
> 4) Menerapkan Distributive Law [Jika bisa] \
> ![applying distributive law](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cdpi%7B150%7D%20%5C%5C%20p%20%5Cvee%20%28q%20%5Cwedge%20r%29%20%5Cequiv%20%28p%20%5Cvee%20q%29%20%5Cwedge%20%28p%20%5Cvee%20r%29%20%5C%5C%20p%20%5Cwedge%20%28q%20%5Cvee%20r%29%20%5Cequiv%20%28p%20%5Cwedge%20q%29%20%5Cvee%20%28p%20%5Cwedge%20r%29)

***Contoh 1.5:*** \
Pada contoh konversi ini akan mengambil contoh dari pertanyaan yang di ajukkan di [stackoverflow.com](https://stackoverflow.com)
> *How to convert a propositional formula to conjunctive normal form (CNF)?*
> 
> How can I convert this equation to CNF? \
> `¬((p ∨ ¬Q) ⊃ R) ⊃ (P ∧ R))` 
> 
> [stackoverflow.com](https://stackoverflow.com/questions/655261/how-to-convert-a-propositional-formula-to-conjunctive-normal-form-cnf)

Dari pertanyaan yang diajukan tersebut, tanda kurung pada propositions agak membingungkan. Sehingga terdapat dua kemungkinan yang dimaksudkan, yaitu: `¬[({p ∨ ¬Q} ⊃ R) ⊃ (P ∧ R)]` atau `¬([p ∨ ¬Q] ⊃ R) ⊃ (P ∧ R)`.

Jika yang dimaksud adalah `¬[({p ∨ ¬Q} ⊃ R) ⊃ (P ∧ R)]` \
![Possible Propositions (1)](https://user-images.githubusercontent.com/62495819/111029944-90f6e000-843a-11eb-813c-5a31c28a80dc.PNG) \
Bentuk akhirnya adalah `¬p ∧ q ∧ r ∧ p` yang mana merupakan bentuk CNF dan DNF.

Jika yang dimaksud adalah `¬([p ∨ ¬Q] ⊃ R) ⊃ (P ∧ R)` \
![Possible Propositions (2)](https://user-images.githubusercontent.com/62495819/111029949-95bb9400-843a-11eb-8d12-89107bba2582.PNG) \
Bentuk akhirnya adalah `¬p ∨ ¬r` yang mana merupakan bentuk CNF dan DNF.

> **Note:** Selalu lihat referensi, logical equivalent rule ketika konversi ke CNF!

Tools: \
Project ini mengunakan SAT Solver [MiniSAT](minisat.se) untuk menyelesaikan Satisfiability Problem 

Sudoku Database: \
https://www.menneske.no/sudoku/eng/ 

Project Reference: \
https://cse.buffalo.edu/~erdem/cse331/support/sat-solver/index.html \
http://swtv.kaist.ac.kr/courses/cs453-fall12/sudoku.pdf \
https://www.cs.utexas.edu/users/moore/acl2/manuals/current/manual/index-seo.php/SATLINK____DIMACS \
http://www.cs.cmu.edu/~hjain/papers/sudoku-as-SAT.pdf \
https://www.andrew.cmu.edu/user/vipuls/me/SudokuSATProjectReport.pdf 
