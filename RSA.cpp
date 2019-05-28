#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/miller_rabin.hpp>
#include <random>
#include <string>
#include <cmath>
#include <chrono>

namespace mp = boost::multiprecision;
using mp::cpp_int;
using std::string;

class RSA {
	private:
		cpp_int p = 4;
		cpp_int q = 4;
		cpp_int phi;
		cpp_int d;
		cpp_int MakePrime();
		cpp_int ExEuclid(cpp_int a, cpp_int b);
	public:
		const int BitLength = 2048;
		cpp_int n;
		const cpp_int e = 65537;
		void genKey(void);
		cpp_int encode(cpp_int m);
		cpp_int decode(cpp_int c);
		cpp_int toCppInt(string str);
		string toString(cpp_int num);
		void setKeys(cpp_int new_n, cpp_int new_d);
};
print()
void RSA::genKey(void) {
	std::cout << "Making Key Pair is Start..." << std::endl << std::endl;
	std::random_device rnd;
	while(!mp::miller_rabin_test(p, 30, rnd))
		p = RSA::MakePrime();
	while(!mp::miller_rabin_test(q, 30, rnd))
		q = RSA::MakePrime();
	n = p * q;
	phi = (p - 1) * (q - 1);
	d = RSA::ExEuclid(phi, e);
	// std::cout << n << std::endl << std::endl;
	// std::cout << d << std::endl << std::endl;
	std::cout << "Making Key Pair is Complete!" << std::endl << std::endl;
}

cpp_int RSA::encode(cpp_int m) {
	cpp_int c;
	c = mp::powm(m, RSA::e, RSA::n);
	return c;
}

cpp_int RSA::decode(cpp_int c) {
	cpp_int m;
	m = mp::powm(c, RSA::d, RSA::n);
	return m;
}

void RSA::setKeys(cpp_int new_n, cpp_int new_d) {
	n = new_n;
	d = new_d;
}

cpp_int RSA::MakePrime() {
	std::random_device rnd;
	cpp_int prime_num;
	for(int i = 0; i < (BitLength/32); ++i) {
		unsigned int tmp = rnd();
		prime_num <<= 32;
		prime_num |= tmp;
	}
	return prime_num;
}

cpp_int RSA::ExEuclid(cpp_int a, cpp_int b) {
	cpp_int a0 = a, x0 = 1, y0 = 0;
	cpp_int a1 = b % a, x1 = 0, y1 = 1;
	cpp_int q;
	while(a1 != 0) {
		q = a0 / a1;
		cpp_int tmp_a0 = a0, tmp_x0 = x0, tmp_y0 = y0;
		a0 = a1;
		x0 = x1;
		y0 = y1;
		a1 = tmp_a0 - q * a1;
		x1 = tmp_x0 - q * x1;
		y1 = tmp_y0 - q * y1;
	}
	if(y0 < 0) {
		return y0 + phi;
	} else {
		return y0;
	}
}

cpp_int RSA::toCppInt(string str) {
	cpp_int num = 0;
	for(char& c: str) {
		num <<= 8;
		num |= (unsigned int)c;
	}
	return num;
}

string RSA::toString(cpp_int num) {
	string str;
	string num_str = num.str(0, std::ios_base::hex);
	for(int i = 0; i < num_str.size(); i+=2){
		str += char(std::stoi(num_str.substr(i, 2), nullptr, 16));
	}
	return str;
}

int main() {
	RSA rsa_test;
	// rsa_test.genKey();
	cpp_int n("59464125288271134738840072049834600402506719765351797372327898274145118110530755672260578146613475755196273169136835599630387527328805208950110209232336934354572718162177708339013917136456433087141654370771198120191182774804263525407502075718870979795990151620745236238257237819381614548821157477486592631926002603410204051896661540827881334514631252871513793855649665419973443111604588239736751423939378098410087958031481475436843391762275362512739576860983076161468230302630726163492258890112731391046843067469589867605765366296522806829262933040487806247500124523727983326395340513357393164463793855629009109576772958639381774992307611453012424057217335546401016462088574160295009021317180789638531266558809179076830128014710083227583979999835891296979171289039300104227201677476220714493955836657406306144163421346703052264714235290598254467903351496109824956264430745475002179171872585883176313474589422995643360689336359169562787579366454757039874315830895211840308944934670651913743338481274983123156259349986652309736821661000423175594094414835889414226781232499879047727912906809736182231340247496597903261696315415628713446402871522782063259708106597957079992775572958912864831609830490950748534641207506843241784811309521");
	cpp_int d("9879081986338955323504138188787999590803563861713999264383571973219586584485998256856022931478821490495094713910643850172813210820697180448430656852185552302555621333747209795919610750900066274818779205471059174705000199155726097694994928062423779361562793091637916477137263002234264906961941538594595733347732065030903180143290825892762439083194303695088914468167806843350639312131326681939267123973510364152906567084956136297913405397068131697189503835427067660192961098845588697500705171056768228416284348056958580320911444042854270423684557043270690364569347938025089376349122900185167108269859583137596337718719407091315962680303620093823225225804332296391809210590884638501865433977557501489221698255732049789302831533448984168873199683583836057040928943040240270976550021716347046792208174552491497208094908480282307218139675188536724238231613340308848489518313968697935448465131349501678303821755306239191436690593376179093360146156142477313828295786428575099228273389168300079591123739176490593461350626674612564003908336865412478563706053458469355986684433353057660668151854763297583734714910532663685886857775464470999889909517475127531847357599833524074848164165276465042682721472278071590505501778544008699474131982241");
	rsa_test.setKeys(n, d);

	string plain_text = "Secret Secret Secret...";
	cpp_int m_int = rsa_test.toCppInt(plain_text);

	auto start = std::chrono::system_clock::now();
	cpp_int cipher_text = rsa_test.encode(m_int);
	cpp_int decode_text_int = rsa_test.decode(cipher_text);
	auto end = std::chrono::system_clock::now();

	// std::cout << "plain text" << std::endl << plain_text << std::endl << std::endl;
	// std::cout << "plain text (hex)" << std::endl << std::hex <<  m_int << std::endl << std::endl;
	// std::cout << "cipher text (hex)" << std::endl << std::hex << cipher_text << std::endl << std::endl;
	// std::cout << "decode text:" << std::endl << rsa_test.toString(decode_text_int) << std::endl << std::endl;
	// std::cout << "decode text (hex)" << std::endl << decode_text_int << std::endl << std::endl;
	auto msec = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
	// std::cout << "Process Time : " << std::dec <<  msec << " milli sec \n";
	std::cout << std::dec << msec << std::endl;

}
