import { styles } from "@/styles/HeaderStyles";
import { Text, View } from "react-native";

type HeaderProps = {
    title: string;
};

export default function Header({ title }: HeaderProps) {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>{title}</Text>
        </View>
    );
}