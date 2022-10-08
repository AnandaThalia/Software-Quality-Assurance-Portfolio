const request_barru = require("supertest")("http://barru.pythonanywhere.com"); 
//url atau endpoint yang dituju
const expect = require("chai").expect; //import library chai untuk validasi

describe("POST User Info", function () { //deskripsikan function untuk test scenario
    it("Success Login with valid email and password", async function () { //test case 1
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "jagoqaindonesia@gmail.com", password: "sman60jakarta" });
        expect(response.body.status).to.eql('SUCCESS_LOGIN');
        expect(response.body.data).to.eql('Welcome Jago QA');
        expect(response.body.message).to.eql('Anda Berhasil Login');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Empty Email and Password", async function () { //test case 2
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "", password: "" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql('Email tidak valid');
        expect(response.body.message).to.eql('Cek kembali email anda');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Empty Password", async function () { //test case 3
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "ananda@jagoqa.com", password: "" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("User's not found");
        expect(response.body.message).to.eql('Email atau Password Anda Salah');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Empty Email", async function () { //test case 4
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "", password: "ananda" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("Email tidak valid");
        expect(response.body.message).to.eql('Cek kembali email anda');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Correct email and Incorret Password", async function () { //test case 5
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "ananda@jagoqa.com", password: "adaaaaaa" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("User's not found");
        expect(response.body.message).to.eql('Email atau Password Anda Salah');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Incorrect Email and Corret Password", async function () { //test case 6
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "anandd@jagoqa.com", password: "ananda" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("User's not found");
        expect(response.body.message).to.eql('Email atau Password Anda Salah');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Invalid Email Format", async function () { //test case 7
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "ananda@@jagoqa.com", password: "ananda" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("Email tidak valid");
        expect(response.body.message).to.eql('Cek kembali email anda');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Invalid Email Format", async function () { //test case 8
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "txz6jei3opjlu4dqhxd56luiqclmrjtp45ygfrq2fv6waw6vb8egn883eh7bciv8won18c5x5rnjsencvq7lgyyfksq@jagoqa.com", password: "ananda" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("Email/Password melebihin maksimal karakter");
        expect(response.body.message).to.eql('Gagal Login');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Invalid Email Format", async function () { //test case 9
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "ananda@jagoqa.com", password: "rq2fv6waw6vb8egn883eh7bciv8won18c5x5rnjsencvq7lgyyfksq" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("Email/Password melebihin maksimal karakter");
        expect(response.body.message).to.eql('Gagal Login');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

    it("Failed Login with Invalid Email Format", async function () { //test case 10
        const response = await request_barru //await untuk menunggu request endpoint pip hingga sukses
            .post("/login") //tipe http request
            .send({ email: "ananda@jagoqa.com", password: "&&rnjsencvq7lgyyfksq" });
        expect(response.body.status).to.eql('FAILED_LOGIN');
        expect(response.body.data).to.eql("Password tidak valid");
        expect(response.body.message).to.eql('Tidak boleh mengandung symbol');
        expect(response.body).to.include.keys("data", "message", "status"); 
    });

});