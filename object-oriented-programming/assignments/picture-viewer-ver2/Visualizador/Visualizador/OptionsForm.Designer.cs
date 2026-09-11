namespace Visualizador
{
    partial class OptionsForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnOK = new System.Windows.Forms.Button();
            this.lblUserName = new System.Windows.Forms.Label();
            this.txtUserName = new System.Windows.Forms.TextBox();
            this.btnCancel = new System.Windows.Forms.Button();
            this.chkPromptOnExit = new System.Windows.Forms.CheckBox();
            this.grpDefaultBackcolor = new System.Windows.Forms.GroupBox();
            this.optBackgroundDefault = new System.Windows.Forms.RadioButton();
            this.optBackgroundWhite = new System.Windows.Forms.RadioButton();
            this.grpDefaultBackcolor.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(305, 12);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 23);
            this.btnOK.TabIndex = 0;
            this.btnOK.Text = "OK";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // lblUserName
            // 
            this.lblUserName.AutoSize = true;
            this.lblUserName.Location = new System.Drawing.Point(40, 41);
            this.lblUserName.Name = "lblUserName";
            this.lblUserName.Size = new System.Drawing.Size(79, 16);
            this.lblUserName.TabIndex = 1;
            this.lblUserName.Text = "User Name:";
            // 
            // txtUserName
            // 
            this.txtUserName.Location = new System.Drawing.Point(125, 38);
            this.txtUserName.MaxLength = 0;
            this.txtUserName.Name = "txtUserName";
            this.txtUserName.Size = new System.Drawing.Size(139, 22);
            this.txtUserName.TabIndex = 2;
            // 
            // btnCancel
            // 
            this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnCancel.Location = new System.Drawing.Point(304, 38);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(75, 23);
            this.btnCancel.TabIndex = 3;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = true;
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
            // 
            // chkPromptOnExit
            // 
            this.chkPromptOnExit.AutoSize = true;
            this.chkPromptOnExit.Location = new System.Drawing.Point(105, 79);
            this.chkPromptOnExit.Name = "chkPromptOnExit";
            this.chkPromptOnExit.Size = new System.Drawing.Size(173, 20);
            this.chkPromptOnExit.TabIndex = 4;
            this.chkPromptOnExit.Text = "Prompt to confirm on exit";
            this.chkPromptOnExit.UseVisualStyleBackColor = true;
            // 
            // grpDefaultBackcolor
            // 
            this.grpDefaultBackcolor.Controls.Add(this.optBackgroundWhite);
            this.grpDefaultBackcolor.Controls.Add(this.optBackgroundDefault);
            this.grpDefaultBackcolor.Location = new System.Drawing.Point(105, 112);
            this.grpDefaultBackcolor.Name = "grpDefaultBackcolor";
            this.grpDefaultBackcolor.Size = new System.Drawing.Size(220, 72);
            this.grpDefaultBackcolor.TabIndex = 5;
            this.grpDefaultBackcolor.TabStop = false;
            this.grpDefaultBackcolor.Text = "Default Picture Background Color";
            // 
            // optBackgroundDefault
            // 
            this.optBackgroundDefault.AutoSize = true;
            this.optBackgroundDefault.Checked = true;
            this.optBackgroundDefault.Location = new System.Drawing.Point(14, 19);
            this.optBackgroundDefault.Name = "optBackgroundDefault";
            this.optBackgroundDefault.Size = new System.Drawing.Size(102, 20);
            this.optBackgroundDefault.TabIndex = 0;
            this.optBackgroundDefault.TabStop = true;
            this.optBackgroundDefault.Text = "Default Gray";
            this.optBackgroundDefault.UseVisualStyleBackColor = true;
            // 
            // optBackgroundWhite
            // 
            this.optBackgroundWhite.AutoSize = true;
            this.optBackgroundWhite.Location = new System.Drawing.Point(14, 42);
            this.optBackgroundWhite.Name = "optBackgroundWhite";
            this.optBackgroundWhite.Size = new System.Drawing.Size(62, 20);
            this.optBackgroundWhite.TabIndex = 1;
            this.optBackgroundWhite.Text = "White";
            this.optBackgroundWhite.UseVisualStyleBackColor = true;
            // 
            // OptionsForm
            // 
            this.AcceptButton = this.btnOK;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::Visualizador.Properties.Resources.seal_ough;
            this.CancelButton = this.btnCancel;
            this.ClientSize = new System.Drawing.Size(382, 253);
            this.Controls.Add(this.grpDefaultBackcolor);
            this.Controls.Add(this.chkPromptOnExit);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.txtUserName);
            this.Controls.Add(this.lblUserName);
            this.Controls.Add(this.btnOK);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "OptionsForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "OptionsForm";
            this.grpDefaultBackcolor.ResumeLayout(false);
            this.grpDefaultBackcolor.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.Label lblUserName;
        private System.Windows.Forms.TextBox txtUserName;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.CheckBox chkPromptOnExit;
        private System.Windows.Forms.GroupBox grpDefaultBackcolor;
        private System.Windows.Forms.RadioButton optBackgroundWhite;
        private System.Windows.Forms.RadioButton optBackgroundDefault;
    }
}