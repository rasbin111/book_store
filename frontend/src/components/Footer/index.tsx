import { IoLogoFacebook, IoLogoInstagram, IoLogoTwitter } from "react-icons/io";
import { AiFillTikTok } from "react-icons/ai";
import "./styles.scss"

const Footer = () => {
  return (
    <div className="footer-main">
      <div className="footer-bottom">
        <div className="copyright">
          &copy; 2026 Book Store. All rights reserved.
        </div>
        <div className="social-media">
          <a href="https://facebook.com" target="blank">
            <IoLogoFacebook className="sm-icon" />
          </a>
          <a href="" target="blank">
            <IoLogoTwitter className="sm-icon" />
          </a>
          <a href="" target="blank">
            <IoLogoInstagram className="sm-icon" />
          </a>
          <a href="" target="blank">
            <AiFillTikTok className="sm-icon" />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Footer;
