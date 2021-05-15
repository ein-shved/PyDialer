
import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    id: root
    width: pWidth
    height: pHeight

    color: "#202020"

     Rectangle {
        id:btn_green
        width: parent.width/3
        height: parent.height/2
        color:"green"
        radius: 7
        border.width: 0
        anchors.verticalCenter: parent.verticalCenter
        x: 10

        Text {
            id: btn_green_label
            text: "Answer"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                self.answer()
            }
        }
     }
}
