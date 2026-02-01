import optionsIcon from './body/images/options.svg'
import logoIcon from './body/images/logo.svg'
import penIcon from './body/images/pen-tool.svg'
import bellIcon from'./body/images/Bell.svg'
import personIcon from './body/images/person.svg'
function Header(){
    return(
    <div className="header">
        <div className="optionsIcon">
            <button className="optionsBtn">
                <img src={optionsIcon} alt="options" width={40} height={40}/>
            </button>
        </div>
        <div className="logoAndTitle">
         <div className="logo">
            <div className="logoIcon">
                <img className="logoIconImg" src={logoIcon} alt="logo"/>
            </div>
         </div>
        <div className="title"> 
            <p className="titleText">SIMPLY SAID</p>
        </div>
        </div>
        <div className="containerHeader">
            <div className="penIcon">
                <button className="penBtn">
                <img src={penIcon} alt="pen" height={35} width={35}/>
                </button>
            </div>
            <div className="bellIcon">
             <button className="bellBtn">
                <img src={bellIcon} alt="bell" height={40} width={40}/>
             </button>
            </div>
             <div className="personHeaderIcon">
             <button className="personHeaderBtn">
                <img src={personIcon} alt="person" height={35} width={35}/>
             </button>
            </div>
        </div>
    </div>
    );
}
export default Header;