// class 之使用說明
// 將性質相同的 object 用 class 的方式統一定義格式，方便後續的新增
 class Phone {
    constructor(number, year, is_waterproof){
        this.number = number;
        this.year = year;
        this.is_waterproof = is_waterproof;
    }
    phone_age (){
        return 2023 - this.year;
    }
 }

 var phone1 = new Phone ('123', 2022, true);
 var phone2 = new Phone ('aaa', 2018, false);

console.log(phone1.year);
