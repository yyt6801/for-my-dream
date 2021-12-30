public class AESEncoderUtil {
private static final String AES = "AES";
private static final String SP = "SHA1PRNG";
private static final String CHARACTER = "utf-8";
/**
* 对原字符串串进⾏行行加密
* @param content 原字符串串
* @return
*/
public static String encode(String content, String encodeRules) {
try {
KeyGenerator kgt = KeyGenerator.getInstance(AES);
SecureRandom secureRandom = SecureRandom.getInstance(SP);
secureRandom.setSeed(encodeRules.getBytes());
kgt.init(128, secureRandom);
SecretKey secretKey = kgt.generateKey();
byte[] enCodeFormat = secretKey.getEncoded();
SecretKeySpec key = new SecretKeySpec(enCodeFormat, AES);
Cipher cipher = Cipher.getInstance(AES);
byte[] byteContent = content.getBytes(CHARACTER);
cipher.init(Cipher.ENCRYPT_MODE, key);
byte[] result = cipher.doFinal(byteContent);
// 对sign进⾏行行url编码，防⽌止加号变为空格
return URLEncoder.encode(parseByte2HexStr(result), "UTF-
8");
} catch (Exception e) {
throw new RuntimeException("encode error");
}
}

/*
* 对加密的字符串串解密
* @param content 加密的字符串串
* @return
*/
public static String decode(String content, String encodeRules) {
try {
// 对sign进⾏行行解码
content = URLDecoder.decode(content, "UTF-8");
byte[] decryptFrom = parseHexStr2Byte(content);
KeyGenerator kgt = KeyGenerator.getInstance(AES);
SecureRandom secureRandom = SecureRandom.getInstance(SP);
secureRandom.setSeed(encodeRules.getBytes());
kgt.init(128, secureRandom);
SecretKey secretKey = kgt.generateKey();
byte[] enCodeFormat = secretKey.getEncoded();
SecretKeySpec key = new SecretKeySpec(enCodeFormat, AES);
Cipher cipher = Cipher.getInstance(AES);// 创建密码器器
cipher.init(Cipher.DECRYPT_MODE, key);// 初始化
byte[] result = cipher.doFinal(decryptFrom);
return new String(result); // 加密
} catch (Exception e) {
return null;
}
}

/**
* 将16进制转换为⼆二进制
* @param hexStr
* @return
**/
private static byte[] parseHexStr2Byte(String hexStr) {
return Base64.getDecoder().decode(hexStr);
}
public static void main(String[] args) {
String CDNO = "{\"companyCode\": \"test\",\"auth\":
1555407227,\"username\": \"123456789\"}";
String encodeRules = "8N3U2C3I4B5C2J7P83A";
String encode = AESEncoderUtil.encode(CDNO, encodeRules);
System.out.println("encode:" + encode);
String decode = AESEncoderUtil.decode(encode, encodeRules);
System.out.println("decode:" + decode);
System.out.printf("完成");
}
}